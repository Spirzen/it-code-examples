netstat -ano | findstr :3000
netstat -ano | findstr LISTENING
tasklist /FI "PID eq 32088"
taskkill /PID 32088 /T /F
taskkill /IM node.exe /F
where node
where git
cd /d C:\Users\zephyr\Projects\moonlit-api
dir /s /b *.log
type logs\app.log
findstr /I error logs\app.log
ping -n 3 127.0.0.1
curl.exe -I http://localhost:3000
ipconfig /all
arp -a
route print
hostname
whoami
systeminfo
schtasks /query /fo LIST
sc query type= service state= all
