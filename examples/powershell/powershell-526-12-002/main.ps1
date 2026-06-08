try {
    $conn = New-Object System.Data.SqlClient.SqlConnection "Server=...;Database=..."
    $conn.Open()
    # Работа с данными
} catch {
    if ($_.Exception.Message -like "*timeout*") {
        Write-Warning "Таймаут подключения. Перезапуск..."
        $conn.Close()
        Start-Sleep -Seconds 5
        $conn.Open()
    } else {
        throw $_
    }
} finally {
    if ($conn.State -eq 'Open') {
        $conn.Close()
    }
}
