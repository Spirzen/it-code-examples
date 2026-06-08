#!/bin/bash

API_URL="https://api.github.com/repos/spirzen/it-knowledge-base"
OUTPUT_FILE="repo_stats.json"

response=$(curl -s "$API_URL")

stars=$(echo "$response" | jq '.stargazers_count')
forks=$(echo "$response" | jq '.forks_count')
language=$(echo "$response" | jq '.language')

cat > "$OUTPUT_FILE" << EOF
{
  "repository": "spirzen/it-knowledge-base",
  "stars": $stars,
  "forks": $forks,
  "primary_language": "$language",
  "checked_at": "$(date -Iseconds)"
}
EOF

echo "Статистика сохранена в $OUTPUT_FILE"
cat "$OUTPUT_FILE"
