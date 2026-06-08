function Get-ProcessedItems {
    param([string]$Source)
    begin {
        Write-Verbose "Начало обработки"
    }
    process {
        # Обработка каждого элемента конвейера
        $_ | ForEach-Object { 
            # Логика
        }
    }
    end {
        Write-Verbose "Завершение обработки"
    }
}
