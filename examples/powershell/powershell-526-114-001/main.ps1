$age = 25
$licensed = $true

if ($age -ge 18 -and $licensed) {
    'Доступ разрешён'
} elseif ($age -ge 14) {
    'Ограниченный доступ'
} else {
    'Доступ запрещён'
}

# switch —-Regex, -Wildcard, -File — см. Get-Help about_Switch
$level = 'Error'
switch ($level) {
    'Error'   { $host.UI.RawUI.WindowTitle = 'ALERT' }
    'Warning' { Write-Warning 'Проверьте журнал' }
    default   { Write-Verbose 'Штатный режим' }
}
