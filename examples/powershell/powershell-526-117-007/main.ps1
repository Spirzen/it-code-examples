$color = "Red"

switch ($color) {
    "Red", "Orange", "Yellow" {
        Write-Host "Это теплые цвета"
        break
    }
    "Blue", "Green", "Purple" {
        Write-Host "Это холодные цвета"
        break
    }
    default {
        Write-Host "Неизвестный цвет"
        break
    }
}
