function Parse-UserData {
    param(
        [string]$JsonString
    )
    
    $json = $JsonString | ConvertFrom-Json
    return $json
}

function Format-UserName {
    param(
        [string]$FirstName,
        [string]$LastName
    )
    
    return "$FirstName $LastName"
}

function Display-User {
    param(
        [object]$UserData
    )
    
    $fullName = Format-UserName -FirstName $UserData.FirstName -LastName $UserData.LastName
    Write-Host "Пользователь: $fullName"
}
