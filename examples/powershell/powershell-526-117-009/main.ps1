$fileExt = ".txt"

switch ($fileExt) {
    case "*.txt" {
        Write-Host "Текстовый файл"
        break
    }
    case "*.doc" {
        Write-Host "Документ Word"
        break
    }
    default {
        Write-Host "Неизвестный формат"
        break
    }
}
