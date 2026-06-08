param(
    [string]$ConfigPath = (Join-Path $PSScriptRoot 'config.json')
)

if (-not (Test-Path -LiteralPath $ConfigPath)) {
    throw "Конфиг не найден: $ConfigPath"
}

$config = Get-Content -LiteralPath $ConfigPath -Raw -Encoding utf8 |
    ConvertFrom-Json

foreach ($key in @('LogFolder', 'ArchiveFolder')) {
    if (-not $config.$key) { throw "В конфиге отсутствует $key" }
}

$config.OlderThanDays = [int]$config.OlderThanDays
