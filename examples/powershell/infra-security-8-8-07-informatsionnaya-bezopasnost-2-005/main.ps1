$ComputerName = $env:COMPUTERNAME
$Timestamp = (Get-Date).ToUniversalTime().ToString("yyyyMMddTHHmmssZ")
$OutDir = "C:\temp\forensic_$ComputerName"

New-Item -ItemType Directory -Path $OutDir -Force | Out-Null

# Экспорт ключей автозагрузки
reg export "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" "$OutDir\HKLM_Run.reg"
reg export "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" "$OutDir\HKCU_Run.reg"

# Список служб
Get-WmiObject Win32_Service | Select-Object Name,DisplayName,PathName,StartMode,State | 
  Export-Csv "$OutDir\services.csv" -NoTypeInformation

# Сетевые соединения
netstat -ano | Out-File "$OutDir\netstat.txt"

# Архивация и отправка (используем BITS для фоновой передачи)
Compress-Archive -Path $OutDir -DestinationPath "$env:TEMP\forensic.zip"
$SecureKey = ConvertTo-SecureString "AES_KEY_HERE" -AsPlainText -Force
Protect-CmsMessage -To "CN=Collector" -Content "$env:TEMP\forensic.zip" -OutFile "$env:TEMP\forensic.zip.p7m"
Start-BitsTransfer -Source "$env:TEMP\forensic.zip.p7m" -Destination "https://collector.example.com/upload"
