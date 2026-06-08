:: Сведения о системе и пользователе
systeminfo
whoami /all
net user
net localgroup administrators

:: Активные процессы с указанием владельца и PID
tasklist /v /fo csv > processes.csv

:: Службы, запущенные с привилегиями SYSTEM или LocalService с автозапуском
sc queryex type= service state= all | findstr /i "SERVICE_NAME TYPE STATE"
wmic service where "StartMode='Auto' and (StartName='LocalSystem' or StartName='.\LocalService')" get Name,DisplayName,PathName

:: Автозагрузка: реестр и папки Startup
reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /s
reg query "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /s
dir "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
dir "%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
