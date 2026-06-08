$isAdmin = $true
$isOnline = $true

if ($isAdmin) {
    if ($isOnline) {
        Write-Host "Администратор онлайн"
    } else {
        Write-Host "Администратор офлайн"
    }
} else {
    Write-Host "Обычный пользователь"
}

# Альтернативный вариант с использованием -and
if ($isAdmin -and $isOnline) {
    Write-Host "Администратор онлайн"
}
