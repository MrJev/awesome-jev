"""Minimal GitHub REST helpers shared by the maintenance scripts (stdlib only)."""

import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.github.com"
README = os.path.join(os.path.dirname(__file__), "..", "README.md")

# Matches https://github.com/owner/repo and https://github.com/owner/repo/tree/branch
REPO_LINK = re.compile(
    r"\(https://github\.com/([\w.-]+)/([\w.-]+?)(?:/tree/([^)\s]+))?/?\)"
)


def get(path, params=None):
    """GET an API path. Returns parsed JSON, or None on 404."""
    url = path if path.startswith("http") else API + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "awesome-jev-maintenance",
    })
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


# Repos under this heading are other people's lists, not entries: they are not
# checked for health and they do not chart as trending.
NOT_OUR_ENTRIES = "## Related Lists"


def _repos_in(text):
    seen, out = set(), []
    for owner, repo, branch in REPO_LINK.findall(text):
        key = (owner.lower(), repo.lower())
        if key not in seen:
            seen.add(key)
            out.append((owner, repo, branch or None))
    return out


def listed_repos():
    """Our own entries: GitHub repos linked from the README above `Related Lists`.

    Used for health checks and trending, where other people's lists are not ours
    to chart or to keep alive.
    """
    with open(README, encoding="utf-8") as f:
        return _repos_in(f.read().split(NOT_OUR_ENTRIES, 1)[0])


def readme_repos():
    """Every GitHub repo the README links, `Related Lists` included.

    Discovery asks a different question from health and trending: not "is this
    one of ours", but "have we already dealt with this". A competing list we
    added under `Related Lists` has been dealt with, and must not come back as
    a candidate every morning.
    """
    with open(README, encoding="utf-8") as f:
        return _repos_in(f.read())
