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


def listed_repos():
    """GitHub repos linked from the README as (owner, repo, branch_or_None)."""
    with open(README, encoding="utf-8") as f:
        text = f.read()
    seen, out = set(), []
    for owner, repo, branch in REPO_LINK.findall(text):
        key = (owner.lower(), repo.lower())
        if key not in seen:
            seen.add(key)
            out.append((owner, repo, branch or None))
    return out
