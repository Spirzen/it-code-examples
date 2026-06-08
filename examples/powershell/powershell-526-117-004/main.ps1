$userName = ""
$serverName = $null
$processCount = 0

if ($userName) {
    Write-Host "Имя пользователя задано"
} else {
    Write-Host "Имя пользователя не задано"
}

if ($serverName -ne $null) {
    Write-Host "Сервер подключен"
} else {
    Write-Host "Сервер не подключен"
}

if ($processCount -gt 0) {
    Write-Host "Процессы запущены"
} else {
    Write-Host "Нет активных процессов"
}
