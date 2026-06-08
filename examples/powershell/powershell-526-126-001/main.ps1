# Watch-Inbound.ps1 — упрощённый опрос (без FileSystemWatcher)
$folder = 'C:\Inbound'
$stateFile = "$PSScriptRoot\.last-scan"
$executor = Join-Path $PSScriptRoot 'Process-Inbound.ps1'

while ($true) {
    $known = if (Test-Path $stateFile) { Get-Content $stateFile } else { @() }
    $current = Get-ChildItem -LiteralPath $folder -Filter '*.csv' | Select-Object -ExpandProperty Name
    $new = Compare-Object -ReferenceObject $known -DifferenceObject $current |
        Where-Object SideIndicator -eq '=>' |
        Select-Object -ExpandProperty InputObject

    foreach ($name in $new) {
        $full = Join-Path $folder $name
        & pwsh -NoProfile -File $executor -Path $full
        if ($LASTEXITCODE -ne 0) {
            Write-Warning "Исполнитель завершился с кодом $LASTEXITCODE для $name"
        }
    }

    $current | Set-Content $stateFile
    Start-Sleep -Seconds 60
}
