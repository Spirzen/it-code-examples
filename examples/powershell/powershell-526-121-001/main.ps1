$applications = @("Google Chrome", "Mozilla Firefox", "Adobe Reader")

foreach ($app in $applications) {
    Write-Host "Проверка обновлений для $app..."
    # В реальном сценарии здесь вызывается API вендора или проверка версии
    $updateAvailable = $true # Имитация наличия обновления
    
    if ($updateAvailable) {
        Write-Host "Найдено обновление для $app. Запуск установки..."
        # Команда запуска установщика
        # Start-Process "setup.exe" -ArgumentList "/silent"
    } else {
        Write-Host "$app уже актуален."
    }
}
