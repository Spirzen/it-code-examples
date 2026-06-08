$sourceFolder = "C:\Данные"
$date = Get-Date -Format "yyyy-MM-dd"
$archiveName = "Backup_$date.zip"
$destinationPath = "D:\Backups\$archiveName"

Compress-Archive -Path "$sourceFolder\*" -DestinationPath $destinationPath -Force
Write-Host "Архив создан: $destinationPath"

# Удаление старых архивов старше 7 дней
$oldArchives = Get-ChildItem "D:\Backups\" -Filter "*.zip" | Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-7) }
foreach ($oldArchive in $oldArchives) {
    Remove-Item $oldArchive.FullName
    Write-Host "Удален старый архив: $($oldArchive.Name)"
}
