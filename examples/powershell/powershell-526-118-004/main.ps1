$MaxRetries = 3
$TimeoutSeconds = 30

function Connect-Service {
    param(
        [string]$ServiceName
    )
    
    for ($i = 1; $i -le $MaxRetries; $i++) {
        try {
            # Попытка подключения
            break
        } catch {
            if ($i -eq $MaxRetries) { throw "Не удалось подключиться" }
            Start-Sleep -Seconds $TimeoutSeconds
        }
    }
}
