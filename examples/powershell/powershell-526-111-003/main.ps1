try {
    $file = Get-Item -Path $strFilePath -ErrorAction Stop
    
    if ($file.Length -lt 1MB) {
        throw "Файл слишком мал"
    }
    
    Copy-Item -Path $file.FullName -Destination $strDestPath
}
catch {
    Write-Error "Ошибка при работе с файлом: $($_.Exception.Message)"
    # Дополнительная обработка ошибки
}
finally {
    Write-Host "Завершение операции обработки файла."
}
