# Пользователи и группы
getent passwd
getent shadow | cut -d: -f1,2  # только имена и хэши (не полные строки!)
groups
sudo -l -U $(whoami) 2>/dev/null

# Процессы с UID/GID и аргументами
ps auxf
# или более структурированно —
ps -eo pid,ppid,uid,gid,comm,args --forest

# Сетевые соединения и слушающие сокеты
ss -tulnp   # современная замена netstat
lsof -i -P  # альтернатива, показывает процессы по FD
