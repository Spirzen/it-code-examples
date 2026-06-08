$dayOfWeek = "Tuesday"

switch ($dayOfWeek) {
    "Monday" {
        Write-Host "Начало рабочей недели"
        break
    }
    "Tuesday" {
        Write-Host "Среда недели"
        break
    }
    "Friday" {
        Write-Host "Предвкушение выходных"
        break
    }
    default {
        Write-Host "Обычный день"
        break
    }
}
