#!/bin/bash
set -euo pipefail

echo "🔍 X-Engine Environment Checker (v1.2)"
echo "OS: $(lsb_release -ds 2>/dev/null || cat /etc/os-release | grep PRETTY_NAME)"
echo "Java: $(java -version 2>&1 | head -1)"

# Проверка подключения к Kafka
echo -n "Kafka test: "
timeout 5 kafka-broker-api-versions --bootstrap-server "$KAFKA_BOOTSTRAP" &>/dev/null \
  && echo "✅ OK" || echo "❌ FAIL"

# Проверка ClickHouse
echo -n "ClickHouse test: "
curl -sf -u "$CH_USER:$CH_PASS" "$CH_URL/?" -d 'SELECT 1' &>/dev/null \
  && echo "✅ OK" || echo "❌ FAIL"
