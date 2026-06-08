<#
.SYNOPSIS
    Получает информацию о пользователе по имени.

.DESCRIPTION
    Функция получает данные о пользователе из системы по указанному имени и выводит их в консоль.

.PARAMETER Name
    Имя пользователя для поиска.

.EXAMPLE
    Get-UserInfo -Name "JohnDoe"
    
    Выводит информацию о пользователе JohnDoe.
#>
function Get-UserInfo {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name
    )
    
    # Логика получения информации
}
