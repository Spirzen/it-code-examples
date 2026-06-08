param(
    [Parameter(Mandatory)]
    [string]$LogFolder,

    [int]$KeepDays = 30
)

function Write-Log([string]$Message) {
    $line = "{0:u}  {1}" -f (Get-Date), $Message
    Add-Content -Path "$PSScriptRoot\archive.log" -Value $line
    Write-Host $line
}

try {
    Write-Log "Старт архивации: $LogFolder"
    # ... поиск, Compress-Archive, Remove-Item ...
    Write-Log "Готово."
    exit 0
}
catch {
    Write-Log "ОШИБКА: $($_.Exception.Message)"
    exit 1
}
