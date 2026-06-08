$servers = @("Server1", "Server2", "Server3")

foreach ($server in $servers) {
    try {
        $ping = Test-Connection -ComputerName $server -Count 1 -Quiet
        
        if ($ping) {
            Write-Output "Сервер $server доступен"
        } else {
            Write-Output "Сервер $server недоступен"
        }
    } catch {
        Write-Output "Ошибка проверки сервера $server: $_"
    }
}
