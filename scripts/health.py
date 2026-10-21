"""Check every GitHub project in the README for staleness, archival, moves, and deletion.

Prints a Markdown report to stdout. Exits 1 when something needs a maintainer's
attention, 0 when everything is healthy.
"""

import re
import sys
import urllib.request
from datetime import datetime, timezone

from github import get, listed_repos

STALE_DAYS = 60    # mark as "(unmaintained)"
ARCHIVE_DAYS = 90  # move to an "Archived" section
# Entries added before the 10-star bar stay, but an abandoned one should not: an
# entry this small that has also stopped moving is an experiment, not a project.
FAINT_STARS = 5
FAINT_IDLE_DAYS = 30
# ...unless MrJev.com has reviewed it: a review is worth keeping a link to.
SITE = "https://mrjev.com/projects/"
REVIEW_MARKERS = ("Hands-on review", "Checked, not fully reviewed", "Our review")


def reviewed_on_site(owner, repo):
    """True when the project's MrJev.com page carries a review or a note."""
    slug = re.sub(r"[^a-z0-9-]+", "-", f"{owner}-{repo}".lower())
    req = urllib.request.Request(SITE + slug + "/", headers={"User-Agent": "awesome-jev-health"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            page = r.read().decode("utf-8", "replace")
    except Exception:
        return False  # can't tell, so flag it as before
    return any(m in page for m in REVIEW_MARKERS)


def days_since(iso):
    ts = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return (datetime.now(timezone.utc) - ts).days


def check(owner, repo, branch):
    """Return (row, problem_or_None) for one listed project."""
    link = f"[{owner}/{repo}](https://github.com/{owner}/{repo})"
    data = get(f"/repos/{owner}/{repo}")
    if data is None:
        return None, f"{link}: repository not found (deleted or made private). Remove it."

    problems = []
    if data["full_name"].lower() != f"{owner}/{repo}".lower():
        problems.append(f"moved to `{data['full_name']}`; update the link")
    if data["archived"]:
        problems.append("archived by its owner")

    last_push = data["pushed_at"]
    if branch:
        b = get(f"/repos/{data['full_name']}/branches/{branch}")
        if b is None:
            problems.append(f"branch `{branch}` no longer exists; link to where the Jev integration lives now")
        else:
            last_push = b["commit"]["commit"]["committer"]["date"]

    idle = days_since(last_push)
    stars = data["stargazers_count"]
    if (stars < FAINT_STARS and idle >= FAINT_IDLE_DAYS and not data["archived"]
            and not reviewed_on_site(owner, repo)):
        problems.append(
            f"{stars} stars and no commits for {idle} days; below the {FAINT_STARS}-star floor "
            "for an inactive entry, so remove it unless it is the only client for its language"
        )
    if idle >= ARCHIVE_DAYS:
        problems.append(f"no commits for {idle} days; move to Archived")
    elif idle >= STALE_DAYS:
        problems.append(f"no commits for {idle} days; mark as (unmaintained)")

    row = f"| {link} | {stars} | {last_push[:10]} | {idle} |"
    problem = f"{link}: " + "; ".join(problems) + "." if problems else None
    return row, problem


def main():
    rows, problems = [], []
    for owner, repo, branch in listed_repos():
        row, problem = check(owner, repo, branch)
        if row:
            rows.append(row)
        if problem:
            problems.append(problem)

    print("Automated weekly check of every GitHub project listed in the README.\n")
    if problems:
        print("## Needs attention\n")
        for p in problems:
            print(f"- [ ] {p}")
        print()
    else:
        print("All listed projects look healthy.\n")
    print(f"<details><summary>All {len(rows)} projects</summary>\n")
    print("| Project | Stars | Last commit | Days idle |")
    print("|---|---:|---|---:|")
    print("\n".join(rows))
    print("\n</details>")
    print(
        f"\nThresholds: unmaintained after {STALE_DAYS} days, archive after {ARCHIVE_DAYS} days, "
        f"remove when under {FAINT_STARS} stars and idle for {FAINT_IDLE_DAYS} days. "
        "New entries need 10+ stars (CONTRIBUTING.md); entries added before that bar are not removed for stars alone."
    )
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
