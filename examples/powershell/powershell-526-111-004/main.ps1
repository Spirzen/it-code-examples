function Send-Notification {
    param(
        [string]$Message,
        [string]$Level
    )
    
    switch ($Level) {
        'Info' { Write-Host $Message }
        'Warning' { Write-Warning $Message }
        'Error' { Write-Error $Message }
    }
}

Send-Notification -Message "Запуск завершен" -Level "Info"
