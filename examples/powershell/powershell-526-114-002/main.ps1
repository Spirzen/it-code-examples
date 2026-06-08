$directory = "C:\Temp"
$extension = ".txt"

if (Test-Path $directory) {
    $files = Get-ChildItem -Path $directory -Filter "*$extension"
    
    foreach ($file in $files) {
        if ($file.Length -gt 1KB) {
            Write-Output "Большой файл: $($file.Name)"
        } elseif ($file.CreationTime -lt (Get-Date).AddDays(-30)) {
            Write-Output "Старый файл: $($file.Name)"
        }
    }
} else {
    Write-Output "Директория не найдена"
}
