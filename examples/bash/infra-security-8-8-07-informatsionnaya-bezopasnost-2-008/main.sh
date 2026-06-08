# Фильтруем login-попытки
awk '$7 == "/login" && $9 ~ /^(401|403)$/ {print $1, $4}' access.log | \
  awk '{
    gsub(/\[|\]/, "", $2);
    split($2, dt, ":");
    time = mktime("2025 11 " dt[1] " " dt[2] " " dt[3] " " dt[4]);
    window = int(time / 60);  # 1-минутное окно
    ip_count[$1, window]++;
    if (ip_count[$1, window] > 10) {
      print "Bruteforce alert: IP", $1, "at window", window;
      # Сброс счётчика, чтобы не дублировать
      delete ip_count[$1, window];
    }
  }'
