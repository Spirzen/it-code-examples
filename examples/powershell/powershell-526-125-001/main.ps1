function Set-ArchiveFilePath {
    [CmdletBinding()]
    [OutputType([string])]
    param(
        [Parameter(Mandatory)]
        [string]$ZipPath,

        [Parameter(Mandatory)]
        [string]$ZipPrefix,

        [Parameter(Mandatory)]
        [datetime]$Date
    )

    if (-not (Test-Path -LiteralPath $ZipPath)) {
        New-Item -Path $ZipPath -ItemType Directory -Force | Out-Null
        Write-Verbose "Создана папка: $ZipPath"
    }

    $zipName = '{0}{1:yyyyMMdd}.zip' -f $ZipPrefix, $Date
    $zipFile = Join-Path -Path $ZipPath -ChildPath $zipName

    if (Test-Path -LiteralPath $zipFile) {
        throw "Архив уже существует: $zipFile"
    }

    return $zipFile
}
