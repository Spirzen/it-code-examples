param(
    [string]$Name = 'Spooler'
)

$svc = Get-Service -Name $Name -ErrorAction SilentlyContinue
if (-null -eq $svc) {
    Write-Error "Service not found: $Name"
    exit 1
}

[PSCustomObject]@{
    Name        = $svc.Name
    Status      = $svc.Status
    DisplayName = $svc.DisplayName
} | Format-List
