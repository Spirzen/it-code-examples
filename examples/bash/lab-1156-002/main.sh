ss -tlnp | grep :3000
lsof -i :3000
ps -p 32088 -o pid,cmd
kill 32088
pkill -f vite
pgrep -af node
curl -I http://localhost:3000
dig +short example.com
nc -zv localhost 3000
df -h
du -sh .
find . -name '*.ts' -mtime -1
grep -RIn TODO src/
tail -f logs/app.log
tar -czf /tmp/backup.tgz .
chmod +x script.sh
