#!/usr/bin/env bash
set -euo pipefail

URL="${1:-http://127.0.0.1:8080/health}"
TIMEOUT="${2:-5}"

STATUS="$(curl -fsS -o /dev/null -w '%{http_code}' --max-time "$TIMEOUT" "$URL" || echo "000")"

if [[ "$STATUS" == "200" ]]; then
  echo "OK $URL"
  exit 0
fi

echo "FAIL $URL status=$STATUS" >&2
exit 1
