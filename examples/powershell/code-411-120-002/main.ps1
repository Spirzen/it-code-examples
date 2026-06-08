#Requires -RunAsAdministrator
$ErrorActionPreference = "Stop"

$AppName     = "MyDemoApp"
$Version     = "1.0.0"
$InstallRoot = Join-Path $env:ProgramFiles $AppName
$PayloadDir  = Join-Path $PSScriptRoot "payload"
$UninstallKey = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\$AppName"

if (-not (Test-Path $PayloadDir)) {
    throw "Не найдена папка payload рядом со скриптом."
}

$requiredMb = 50
$drive = (Split-Path $InstallRoot -Qualifier)
$freeMb = (Get-PSDrive ($drive.TrimEnd(':'))).Free / 1MB
if ($freeMb -lt $requiredMb) {
    throw "Недостаточно места на диске (нужно ~$requiredMb МБ)."
}

if (Test-Path $InstallRoot) {
    Write-Host "Обновление: удаляем предыдущую копию..."
    Remove-Item $InstallRoot -Recurse -Force
}
New-Item -ItemType Directory -Path $InstallRoot -Force | Out-Null
Copy-Item -Path (Join-Path $PayloadDir "*") -Destination $InstallRoot -Recurse -Force

$exePath = Join-Path $InstallRoot "MyApp.exe"
$uninstallScript = Join-Path $InstallRoot "uninstall.ps1"
@'
Remove-Item -LiteralPath $PSScriptRoot -Recurse -Force
Remove-Item -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\MyDemoApp" -ErrorAction SilentlyContinue
'@ | Set-Content -Path $uninstallScript -Encoding UTF8

New-Item -Path $UninstallKey -Force | Out-Null
Set-ItemProperty -Path $UninstallKey -Name DisplayName -Value $AppName
Set-ItemProperty -Path $UninstallKey -Name DisplayVersion -Value $Version
Set-ItemProperty -Path $UninstallKey -Name Publisher -Value "IT Universe"
Set-ItemProperty -Path $UninstallKey -Name InstallLocation -Value $InstallRoot
Set-ItemProperty -Path $UninstallKey -Name UninstallString -Value "powershell.exe -ExecutionPolicy Bypass -File `"$uninstallScript`""

$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$env:ProgramData\Microsoft\Windows\Start Menu\Programs\$AppName.lnk")
$Shortcut.TargetPath = $exePath
$Shortcut.WorkingDirectory = $InstallRoot
$Shortcut.Save()

Write-Host "Установлено в $InstallRoot"
