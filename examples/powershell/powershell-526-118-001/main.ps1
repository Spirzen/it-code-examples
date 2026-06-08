function Get-LogLines {
    param(
        [Parameter(ValueFromPipeline = $true)]
        [string]$LogFile
    )
    
    Begin {
        Write-Host "Начало обработки логов..."
        $startTime = Get-Date
    }
    
    Process {
        Get-Content -Path $LogFile | ForEach-Object {
            Write-Host "Чтение строки: $_"
        }
    }
    
    End {
        Write-Host "Завершение обработки..."
        $endTime = Get-Date
        Write-Host "Время выполнения: $($endTime - $startTime)"
    }
}
