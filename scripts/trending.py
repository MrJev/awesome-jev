"""Keep a daily star snapshot of every listed project and rewrite the trending table.

    python scripts/trending.py            # snapshot today, rewrite the README block
    python scripts/trending.py --dry-run  # print the block, touch nothing

Snapshots live in data/stars.json and are committed, so growth is computed from
our own history rather than from an API that only owners can read. The README
block between the trending markers is generated; everything else is hand-written.
"""

import json
import os
import sys
from datetime import datetime, timedelta, timezone

from github import REPO_LINK, get

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "stars.json")
README = os.path.join(os.path.dirname(__file__), "..", "README.md")
START = "<!-- trending:start -->"
END = "<!-- trending:end -->"
STATS = os.path.join(os.path.dirname(__file__), "..", "data", "stats.json")
STATS_START = "<!-- stats:start -->"
STATS_END = "<!-- stats:end -->"

HISTORY_DAYS = 45  # snapshots older than this are dropped
WINDOW_DAYS = 7  # growth window
TOP_N = 10  # rows in the trending table
NEW_N = 5  # rows in the new-this-week list
MIN_GAIN = 5  # below this a project is not "trending"

LIST_LAUNCH = "2026-09-18"  # first snapshot: everything was "new", so it is not


def today():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def project_repos():
    """GitHub repos linked from the list itself, ignoring the Related Lists section:
    those are other people's lists, not entries, and must not chart as trending."""
    with open(README, encoding="utf-8") as f:
        text = f.read().split("## Related Lists", 1)[0]
    seen, out = set(), []
    for owner, repo, branch in REPO_LINK.findall(text):
        key = (owner.lower(), repo.lower())
        if key not in seen:
            seen.add(key)
            out.append((owner, repo, branch or None))
    return out


def load():
    if not os.path.exists(DATA):
        return {"snapshots": {}, "firstSeen": {}}
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)


def snapshot(repos):
    """Current star count and description for each listed repo, keyed owner/repo."""
    out = {}
    for owner, repo, _branch in repos:
        data = get(f"/repos/{owner}/{repo}")
        if data is None or data.get("archived"):
            continue
        out[data["full_name"]] = data["stargazers_count"]
    return out


def baseline(snapshots, cutoff):
    """The newest snapshot at or before `cutoff`, else the oldest one we have."""
    dates = sorted(snapshots)
    older = [d for d in dates if d <= cutoff]
    return snapshots[older[-1]] if older else (snapshots[dates[0]] if dates else {})


def table(rows):
    """A pipe-aligned Markdown table. Names are plain text: awesome-lint rejects a
    second link to a repository the list already links to."""
    header = ["Project", "Stars", "This week"]
    body = [[full_name, f"{stars:,}", f"+{gained:,}"] for full_name, stars, gained in rows]
    width = [max(len(r[i]) for r in [header, *body]) for i in range(3)]
    line = lambda cells: "| " + " | ".join(
        c.ljust(width[i]) if i == 0 else c.rjust(width[i]) for i, c in enumerate(cells)
    ) + " |"
    rule = "| " + " | ".join(("-" * width[0], *("-" * (width[i] - 1) + ":" for i in (1, 2)))) + " |"
    return [line(header), rule, *(line(r) for r in body)]


def block(store):
    snapshots = store["snapshots"]
    current_date = max(snapshots)
    current = snapshots[current_date]
    cutoff = (datetime.strptime(current_date, "%Y-%m-%d") - timedelta(days=WINDOW_DAYS)).strftime("%Y-%m-%d")
    was = baseline({d: s for d, s in snapshots.items() if d != current_date}, cutoff)

    growth = []
    for full_name, stars in current.items():
        before = was.get(full_name)
        if before is None:
            continue
        gained = stars - before
        if gained >= MIN_GAIN:
            growth.append((full_name, stars, gained))
    growth.sort(key=lambda r: (-r[2], -r[1]))

    fresh_cutoff = (datetime.strptime(current_date, "%Y-%m-%d") - timedelta(days=WINDOW_DAYS)).strftime("%Y-%m-%d")
    fresh = [
        (full_name, current[full_name], store["firstSeen"][full_name])
        for full_name in current
        if store["firstSeen"].get(full_name, LIST_LAUNCH) > fresh_cutoff
        and store["firstSeen"].get(full_name) != LIST_LAUNCH
    ]
    fresh.sort(key=lambda r: (-r[1]))

    lines = [START, "", "## Trending", "", f"Stars gained in the last {WINDOW_DAYS} days, from our own daily snapshots. Updated {current_date}."]
    if growth:
        lines += ["", *table(growth[:TOP_N])]
    else:
        lines += ["", "_No project gained enough stars this week to chart._"]
    if fresh:
        lines += [
            "",
            "**New to this list this week:** "
            + ", ".join(f"`{n}`" for n, _s, _d in fresh[:NEW_N])
            + (f" and {len(fresh) - NEW_N} more" if len(fresh) > NEW_N else "")
            + ".",
        ]
    lines += ["", "Sortable, with hands-on reviews: [mrjev.com/projects](https://mrjev.com/projects/?sort=rising).", "", END]
    return "\n".join(lines)


def entry_count(readme):
    """List items that are entries: a linked project or resource, one per line."""
    body = readme.split("## Official Resources", 1)[-1].split("## Related Lists", 1)[0]
    return sum(1 for line in body.split("\n") if line.startswith("- ["))


def stats_line(readme):
    return f"**{entry_count(readme)} entries \u00b7 every one checked to actually call Jev \u00b7 last reviewed {today()}**"


def replace_block(text, start, end, body):
    head, rest = text.split(start, 1)
    _old, tail = rest.split(end, 1)
    return head + start + "\n" + body + "\n" + end + tail


def main():
    dry = "--dry-run" in sys.argv
    store = load()
    repos = project_repos()
    current = snapshot(repos)
    if len(current) < 10:
        print(f"only {len(current)} repos resolved; refusing to overwrite history", file=sys.stderr)
        return 2

    store["snapshots"][today()] = current
    keep = (datetime.now(timezone.utc) - timedelta(days=HISTORY_DAYS)).strftime("%Y-%m-%d")
    store["snapshots"] = {d: s for d, s in store["snapshots"].items() if d >= keep}
    for full_name in current:
        store["firstSeen"].setdefault(full_name, today())

    text = block(store)
    if dry:
        print(text)
        return 0

    with open(README, encoding="utf-8") as f:
        readme = f.read()
    if START not in readme or END not in readme:
        print(f"README is missing the {START} / {END} markers", file=sys.stderr)
        return 2
    head, rest = readme.split(START, 1)
    _old, tail = rest.split(END, 1)
    readme = head + text + tail
    if STATS_START in readme and STATS_END in readme:
        readme = replace_block(readme, STATS_START, STATS_END, stats_line(readme))
    with open(README, "w", encoding="utf-8") as f:
        f.write(readme)
    with open(STATS, "w", encoding="utf-8") as f:
        json.dump({"entries": entry_count(readme), "updated": today()}, f, indent=1)
        f.write("\n")

    os.makedirs(os.path.dirname(DATA), exist_ok=True)
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(store, f, indent=1, sort_keys=True)
        f.write("\n")
    print(f"snapshot {today()}: {len(current)} repos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
