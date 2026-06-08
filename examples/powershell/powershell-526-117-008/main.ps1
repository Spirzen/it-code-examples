$email = "user@example.com"

switch ($email) {
    { $_ -match "@gmail\.com$" } {
        Write-Host "Почта Gmail"
        break
    }
    { $_ -match "@yahoo\.com$" } {
        Write-Host "Почта Yahoo"
        break
    }
    default {
        Write-Host "Другой провайдер"
        break
    }
}
