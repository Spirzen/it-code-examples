[CmdletBinding()]
function Get-SystemInfo {
    param(
        [switch]$Detailed
    )
    
    Write-Verbose "Получение информации о системе..."
    
    if ($Detailed) {
        Get-CimInstance Win32_OperatingSystem | Select-Object *
    } else {
        Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version
    }
}
