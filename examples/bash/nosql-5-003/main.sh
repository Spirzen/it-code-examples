#!/bin/bash
REDIS_CLI="redis-cli -u redis://appuser:Str0ngP@ss@127.0.0.1:6379"

# Проверка доступности
if ! $REDIS_CLI PING | grep -q "PONG"; then
  echo "CRITICAL: Redis не отвечает"
  exit 2
fi

# Проверка памяти
USED_MB=$($REDIS_CLI INFO memory | grep used_memory_human | cut -d: -f2 | sed 's/M.*//')
MAX_MB=512

if (( $(echo "$USED_MB > $MAX_MB * 0.9" | bc -l) )); then
  echo "WARNING: Память Redis заполнена на >90% ($USED_MB MB / $MAX_MB MB)"
  exit 1
fi

# Проверка hit rate
HITS=$($REDIS_CLI INFO stats | grep keyspace_hits | cut -d: -f2)
MISSES=$($REDIS_CLI INFO stats | grep keyspace_misses | cut -d: -f2)
TOTAL=$((HITS + MISSES))

if [ $TOTAL -gt 0 ]; then
  HIT_RATE=$(echo "scale=2; $HITS / $TOTAL * 100" | bc)
  echo "OK: Hit rate = ${HIT_RATE}%, Memory = ${USED_MB} MB"
else
  echo "OK: Нет запросов, Memory = ${USED_MB} MB"
fi
exit 0
