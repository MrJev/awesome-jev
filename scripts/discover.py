"""Find new GitHub repositories that use Jev and are not yet in the README.

Prints a Markdown report to stdout. Exits 1 when there are candidates to review,
0 when there is nothing new.

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
SINCE = "2026-09-01"  # Jev launched 2026-09-15; nothing older is relevant
MIN_STARS = 5  # below this, a repo resurfaces automatically once it gains traction

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

    print(f"Automated weekly search found {len(ranked)} repositories with {MIN_STARS}+ stars that "
          f"mention Jev / TypeSafe and are not in the list yet ({below} with fewer stars are not shown).\n")
    print("For each one: check that it actually calls Jev and has a usable README, then either "
          "add it to the README (write your own description) or add `owner/repo` to "
          "`.github/discovery-ignore.txt`. Checked items disappear on the next run.\n")
    print("| Repository | Stars | Created | Description |")
    print("|---|---:|---|---|")
    for r in ranked:
        desc = (r.get("description") or "").replace("|", "\\|")[:140]
        print(f"| [{r['full_name']}]({r['html_url']}) | {r['stargazers_count']} "
              f"| {r['created_at'][:10]} | {desc} |")
    return 1


if __name__ == "__main__":
    sys.exit(main())
