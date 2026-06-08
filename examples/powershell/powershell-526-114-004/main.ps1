function Configure-User {
    param(
        [string]$Username,
        [ValidateSet("Admin", "User", "Guest")]
        [string]$Role = "User",
        [switch]$EnableRemoteAccess
    )
    
    Write-Output "Настройка пользователя: $Username"
    Write-Output "Роль: $Role"
    
    if ($EnableRemoteAccess.IsPresent) {
        Write-Output "Удаленный доступ включен"
    }
}

Configure-User -Username "Ivan" -Role "Admin" -EnableRemoteAccess
