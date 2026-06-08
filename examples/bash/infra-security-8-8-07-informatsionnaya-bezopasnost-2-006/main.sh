#!/bin/bash
# normalize_logs.sh

while IFS= read -r line; do
  # Извлекаем исходные поля (пример для auth.log)
  if [[ $line =~ ^([A-Za-z]+)\ +([0-9]+)\ +([0-9:]+)\ +([^ ]+)\ +sshd\[([0-9]+)\]:\ Accepted\ ([^ ]+)\ for\ ([^ ]+)\ from\ ([^ ]+) ]]; then
    month="${BASH_REMATCH[1]}"
    day="${BASH_REMATCH[2]}"
    time="${BASH_REMATCH[3]}"
    host="${BASH_REMATCH[4]}"
    pid="${BASH_REMATCH[5]}"
    method="${BASH_REMATCH[6]}"
    user="${BASH_REMATCH[7]}"
    ip="${BASH_REMATCH[8]}"

    # Нормализуем месяц
    declare -A MONTHS=( ["Jan"]="01" ["Feb"]="02" ["Mar"]="03" ["Apr"]="04" ["May"]="05" ["Jun"]="06"
                        ["Jul"]="07" ["Aug"]="08" ["Sep"]="09" ["Oct"]="10" ["Nov"]="11" ["Dec"]="12" )
    month_num="${MONTHS[$month]}"

    # Генерируем ISO-время (год подставляем как 2025)
    iso_time="2025-${month_num}-${day}T${time}Z"

    # Формируем JSON
    jq -n --arg ts "$iso_time" \
         --arg h "$(hostname -f)" \
         --arg src "$ip" \
         --arg u "$user" \
         --arg m "$method" \
         '{timestamp: $ts, host: $h, source: "sshd", event_id: "auth_success", user: $u, src_ip: $src, auth_method: $m}'
  fi
done
