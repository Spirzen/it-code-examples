$age = 25
$status = "active"

# Пример использования -and
if ($age -ge 18 -and $status -eq "active") {
    Write-Host "Пользователь активен и старше 18 лет"
}

# Пример использования -or
if ($status -eq "active" -or $status -eq "suspended") {
    Write-Host "Статус пользователя либо активен, либо приостановлен"
}

# Пример использования -xor
$x = $true
$y = $false
if ($x -xor $y) {
    Write-Host "Истинно ровно одно из условий"
}

# Пример использования -not
if (-not ($status -eq "inactive")) {
    Write-Host "Статус не является неактивным"
}

# Использование краткой формы !
if (!($age -lt 18)) {
    Write-Host "Возраст не меньше 18"
}
