#!/usr/bin/env bash
set -euo pipefail

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TMP_DIR=""

log() { printf '[%s] %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*"; }

cleanup() {
  local code=$?
  [[ -n "$TMP_DIR" && -d "$TMP_DIR" ]] && rm -rf "$TMP_DIR"
  exit "$code"
}
trap cleanup EXIT INT TERM

usage() {
  echo "Usage: $0 -i <input> -o <output>"
  echo "  -i  input file"
  echo "  -o  output file"
  echo "  -h  help"
}

INPUT=""
OUTPUT=""
while getopts "i:o:h" opt; do
  case "$opt" in
    i) INPUT="$OPTARG" ;;
    o) OUTPUT="$OPTARG" ;;
    h) usage; exit 0 ;;
    *) usage; exit 1 ;;
  esac
done

[[ -f "$INPUT" ]] || { log "Input not found: $INPUT"; exit 1; }
TMP_DIR="$(mktemp -d)"
cp "$INPUT" "$TMP_DIR/in.txt"
tr '[:lower:]' '[:upper:]' < "$TMP_DIR/in.txt" > "$OUTPUT"
log "Done: $OUTPUT"
