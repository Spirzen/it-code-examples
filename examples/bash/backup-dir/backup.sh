#!/usr/bin/env bash
set -euo pipefail

SRC="${1:-./data}"
STAMP="$(date +%Y%m%d-%H%M)"
ARCHIVE="backup-${STAMP}.tar.gz"

tar -czf "$ARCHIVE" -C "$(dirname "$SRC")" "$(basename "$SRC")"
echo "Created $ARCHIVE"
