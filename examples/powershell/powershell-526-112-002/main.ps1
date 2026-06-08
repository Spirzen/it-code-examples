<#
    .SYNOPSIS
        Создает резервную копию папки.

    .DESCRIPTION
        Данный скрипт копирует содержимое указанной папки 
        в архив с расширением .zip.

    .PARAMETER SourcePath
        Полный путь к исходной папке.

    .PARAMETER DestinationPath
        Полный путь к месту сохранения архива.

    .EXAMPLE
        .\Backup.ps1 -SourcePath "C:\Данные" -DestinationPath "C:\Backup"
#>
