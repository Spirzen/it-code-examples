$filename = "report_2024.pdf"

# Проверка по простому шаблону
if ($filename -like "*.pdf") {
    Write-Host "Файл является PDF документом"
}

# Проверка с учетом регистра (если нужно)
if ($filename -clike "REPORT*.PDF") {
    Write-Host "Найдено совпадение с учетом регистра"
}

# Использование регулярного выражения
if ($filename -match "\d{4}") {
    Write-Host "В имени файла найдены четыре цифры подряд"
}

# Получение совпавшей части
if ($filename -match "(?<year>\d{4})") {
    Write-Host "Год найден: $($Matches.year)"
}
