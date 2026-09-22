#!/usr/bin/env bash
# Keep one rolling issue per label: create or update it, or close it when resolved.
#
# One issue per label answers "what is pending now". It is updated in place rather than
# reopened daily, so an item that sits unhandled for a week appears once, not seven times;
# GitHub keeps every body edit, so the history is still there (GraphQL userContentEdits).
#
#   issue.sh open  LABEL TITLE BODY_FILE
#   issue.sh close LABEL
#
# Needs GH_TOKEN and GH_REPO in the environment (set by the workflows).
set -euo pipefail

mode=$1
label=$2
run_url="${GITHUB_SERVER_URL:-https://github.com}/${GH_REPO}/actions/runs/${GITHUB_RUN_ID:-0}"

gh label create "$label" --color BFD4F2 --description "Opened by maintenance automation" --force >/dev/null
existing=$(gh issue list --label "$label" --state open --limit 1 --json number --jq '.[0].number // empty')

case "$mode" in
  open)
    title=$3
    body_file=$4
    if [[ -n "$existing" ]]; then
      # Editing an issue does not notify anyone; commenting does. Comment only when the
      # body actually changed, so a run that finds the same backlog stays silent while
      # the title still records that it ran.
      before=$(gh issue view "$existing" --json body --jq .body)
      if [[ "$before" == "$(cat "$body_file")" ]]; then
        gh issue edit "$existing" --title "$title"
        echo "Issue #$existing unchanged; title refreshed, no comment."
      else
        gh issue edit "$existing" --title "$title" --body-file "$body_file"
        gh issue comment "$existing" --body "Updated by $run_url"
      fi
    else
      gh issue create --title "$title" --label "$label" --body-file "$body_file"
    fi
    ;;
  close)
    if [[ -n "$existing" ]]; then
      gh issue close "$existing" --comment "Resolved: nothing left to do as of $run_url"
    fi
    ;;
  *)
    echo "unknown mode: $mode" >&2
    exit 2
    ;;
esac
