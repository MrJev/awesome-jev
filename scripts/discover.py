"""Find new GitHub repositories that use Jev and are not yet in the README.

Prints a Markdown report to stdout. Exits 1 when there are candidates to review,
0 when there is nothing new. Writes a one-line issue title to $DISCOVERY_TITLE_FILE
when that is set, so the issue title carries the pending count and the run date.

The report is compared against the currently open discovery issue so it can say
what changed. That is the only reason this script reads an issue: a rolling issue
answers "what is pending now" but not "what is new since I last looked".

Rejected candidates go in .github/discovery-ignore.txt (one owner/repo per line)
so they are not suggested again.
"""

import base64
import os
import re
import sys
import time

from github import get, listed_repos

IGNORE_FILE = os.path.join(os.path.dirname(__file__), "..", ".github", "discovery-ignore.txt")
ISSUE_LABEL = "discovery"
CANDIDATE_ROW = re.compile(r"^\| \[([\w.-]+/[\w.-]+)\]\(", re.M)
MAX_NAMED_NEW = 15  # past this, the delta line names a count instead of every repo
SINCE = "2026-09-01"  # Jev launched 2026-09-15; nothing older is relevant
MIN_STARS = 10  # the inclusion bar in CONTRIBUTING.md; below this, a repo resurfaces automatically once it gains traction

QUERIES = [
    f"jev typesafe in:name,description,readme created:>={SINCE}",
    f"\"system one\" typesafe in:name,description,readme created:>={SINCE}",
    f"typesafe.ai in:description,readme created:>={SINCE}",
    f"topic:jev created:>={SINCE}",
    f"jev in:name created:>={SINCE}",  # noisy; confirmed below via README
]

# "JEV" is also Japanese encephalitis virus, and "typesafe" is a common word.
# Require an unambiguous TypeSafe AI signal, or both "jev" and "typesafe".
STRONG = re.compile(r"typesafe[ .-]?ai|system[ -]?one", re.I)


def is_signal(text):
    return bool(STRONG.search(text)) or (
        re.search(r"\bjev\b", text, re.I) is not None and re.search(r"typesafe", text, re.I) is not None
    )


def load_ignore():
    try:
        with open(IGNORE_FILE, encoding="utf-8") as f:
            return {line.strip().lower() for line in f if line.strip() and not line.startswith("#")}
    except FileNotFoundError:
        return set()


def mentions_typesafe(repo):
    text = " ".join([repo["name"], repo.get("description") or "", " ".join(repo.get("topics") or [])])
    if is_signal(text):
        return True
    readme = get(f"/repos/{repo['full_name']}/readme", {})
    if not readme:
        return False
    body = base64.b64decode(readme.get("content", "")).decode("utf-8", "replace")
    return is_signal(body)


def search(query):
    """Yield every result for a repository search (the API caps this at 1000)."""
    for page in range(1, 11):
        res = get("/search/repositories", {"q": query, "sort": "updated", "per_page": 100, "page": page}) or {}
        items = res.get("items", [])
        yield from items
        if len(items) < 100:
            return
        time.sleep(2)  # stay under the search rate limit (30 requests/minute)


def previous_candidates():
    """Repo names listed by the open discovery issue, or None when there is no list to compare.

    Never raises: a delta is a convenience, and losing it must not cost us the report.
    """
    repo = os.environ.get("GITHUB_REPOSITORY", "MrJev/awesome-jev")
    try:
        issues = get(f"/repos/{repo}/issues", {"labels": ISSUE_LABEL, "state": "open", "per_page": 1})
    except Exception:
        return None
    if not issues:
        return None
    return {name.lower() for name in CANDIDATE_ROW.findall(issues[0].get("body") or "")}


def format_delta(current, previous):
    """One line saying what changed, and which repos are new. Empty when there is no baseline."""
    if previous is None:
        return ""
    new = [r for r in current if r["full_name"].lower() not in previous]
    gone = len(previous - {r["full_name"].lower() for r in current})
    if not new and not gone:
        return "Unchanged since the previous run.\n"

    line = (f"Since the previous run: **{len(new)} new**, **{gone} gone** "
            f"(added to the list, ignored, or no longer matching).")
    if not new:
        return line + "\n"
    if len(new) > MAX_NAMED_NEW:
        return line + f" The {len(new)} new ones are marked **new** in the table below.\n"
    named = " · ".join(f"[{r['full_name']}]({r['html_url']})" for r in new)
    return f"{line}\n\nNew: {named}\n"


def write_title(pending):
    """The issue title carries the count and the date, so a list view answers 'did it run today'."""
    path = os.environ.get("DISCOVERY_TITLE_FILE")
    if not path:
        return
    day = time.strftime("%-d %b", time.gmtime())
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"New Jev projects to review \u2014 {pending} pending ({day})\n")


def main():
    skip = {f"{o}/{r}".lower() for o, r, _ in listed_repos()} | load_ignore()
    skip.add(os.environ.get("GITHUB_REPOSITORY", "MrJev/awesome-jev").lower())

    found = {}
    for q in QUERIES:
        for repo in search(q):
            name = repo["full_name"].lower()
            if name in skip or name in found:
                continue
            if mentions_typesafe(repo):
                found[name] = repo

    ranked = sorted(
        (r for r in found.values() if r["stargazers_count"] >= MIN_STARS),
        key=lambda r: r["stargazers_count"], reverse=True,
    )
    below = len(found) - len(ranked)
    if not ranked:
        print(f"No new Jev projects with {MIN_STARS}+ stars ({below} smaller ones skipped).")
        return 0

    previous = previous_candidates()
    write_title(len(ranked))

    print(f"Automated daily search found {len(ranked)} repositories with {MIN_STARS}+ stars that "
          f"mention Jev / TypeSafe and are not in the list yet ({below} with fewer stars are not shown).\n")
    delta = format_delta(ranked, previous)
    if delta:
        print(delta)
    print("For each one: check that it actually calls Jev and has a usable README, then either "
          "add it to the README (write your own description) or add `owner/repo` to "
          "`.github/discovery-ignore.txt`. Checked items disappear on the next run.\n")
    print("| Repository | Stars | Created | New | Description |")
    print("|---|---:|---|---|---|")
    for r in ranked:
        desc = (r.get("description") or "").replace("|", "\\|")[:140]
        fresh = "new" if previous is not None and r["full_name"].lower() not in previous else ""
        print(f"| [{r['full_name']}]({r['html_url']}) | {r['stargazers_count']} "
              f"| {r['created_at'][:10]} | {fresh} | {desc} |")
    return 1


if __name__ == "__main__":
    sys.exit(main())
