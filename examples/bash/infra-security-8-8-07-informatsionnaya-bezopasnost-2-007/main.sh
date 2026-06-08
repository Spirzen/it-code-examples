# 1. Извлекаем уникальные user-agent’ы и их частоту
awk -F'"' '{print $6}' access.log | sort | uniq -c | sort -nr > uas.txt

# 2. Ищем известные сигнатуры
grep -Ei "nmap|sqlmap|acunetix|burpsuite|ZmEu" uas.txt

# 3. Определяем "сканерские" IP по поведению —
# >50 запросов за 1 мин, >80% запросов — 404
awk '{
  ip = $1;
  gsub(/\[|\]/, "", $4);
  split($4, dt, ":");
  time = mktime("2025 11 " dt[1] " " dt[2] " " dt[3] " " dt[4]);
  status = $9;
  window = int(time / 60);
  count[ip, window]++;
  if (status == 404) notfound[ip, window]++
}
END {
  for (key in count) {
    split(key, a, SUBSEP);
    ip = a[1]; win = a[2];
    if (count[key] > 50 && (notfound[key] / count[key]) > 0.8)
      print "Scanner candidate:", ip, "window", win
  }
}' access.log
