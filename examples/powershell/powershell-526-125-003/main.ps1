param(
    [Parameter(Mandatory)]
    [string]$LogFolder,

    [Parameter(Mandatory)]
    [string]$ArchiveFolder,

    [string]$ArchivePrefix = 'logs_',

    [int]$OlderThanDays = 30
)

function Write-Log([string]$Message) {
    $line = '{0:u}  {1}' -f (Get-Date), $Message
    Add-Content -Path "$PSScriptRoot\archive.log" -Value $line
    Write-Host $line
}

try {
    Write-Log "Старт: $LogFolder"
    $files = Get-FilesOlderThan -Path $LogFolder -Days $OlderThanDays
    if (-not $files) {
        Write-Log 'Нет файлов для архивации.'
        exit 0
    }

    $lastDate = ($files | Sort-Object LastWriteTime -Descending | Select-Object -First 1).LastWriteTime
    $zipPath = Set-ArchiveFilePath -ZipPath $ArchiveFolder -ZipPrefix $ArchivePrefix -Date $lastDate

    Compress-Archive -Path $files.FullName -DestinationPath $zipPath
    $files | Remove-Item -Force
    Write-Log "Архив: $zipPath"
    exit 0
}
catch {
    Write-Log "ОШИБКА: $($_.Exception.Message)"
    exit 1
}
