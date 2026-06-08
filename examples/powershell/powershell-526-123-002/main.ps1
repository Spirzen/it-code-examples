function Get-Greeting {
    param(
        [string]$Name,
        [string]$Language = "en"
    )
    
    switch ($Language) {
        "ru" { return "Привет, $Name!" }
        "de" { return "Hallo, $Name!" }
        default { return "Hello, $Name!" }
    }
}

$result = Get-Greeting -Name "Timur" -Language "ru"
Write-Host $result
