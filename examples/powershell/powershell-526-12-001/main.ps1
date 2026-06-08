function Log-Error {
    param(
        [Parameter(Mandatory)]
        [string]$Message,
        [ValidateSet("Info", "Warning", "Error", "Critical")]
        [string]$Level = "Error"
    )
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logEntry = "[$timestamp] [$Level] $Message"
    Add-Content -Path "app.log" -Value $logEntry
    Write-Host $logEntry
}

try {
    # Опасный код
} catch {
    Log-Error -Message $_.Exception.Message -Level Error
}
