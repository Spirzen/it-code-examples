# Проверка существования источника
if (-not (Test-Path -Path $SourcePath)) {
    Write-Error "Источник пути не существует: $SourcePath"
    exit 1
}

# Проверка существования места назначения
if (-not (Test-Path -Path $DestinationPath)) {
    Write-Error "Место назначения не существует: $DestinationPath"
    exit 1
}

# Установка политики выполнения для текущего сеанса
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
