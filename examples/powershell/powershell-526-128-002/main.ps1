function Test-ServerHealth {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [pscustomobject]$Server
    )

    $result = [ordered]@{
        Name   = $Server.Name
        Ok     = $true
        Detail = ''
    }

    try {
        if ($Server.Port) {
            $tcp = Test-NetConnection -ComputerName $Server.Host -Port $Server.Port -WarningAction SilentlyContinue
            if (-not $tcp.TcpTestSucceeded) { throw "Port $($Server.Port) closed" }
        }
    }
    catch {
        $result.Ok = $false
        $result.Detail = $_.Exception.Message
    }

    [pscustomobject]$result
}
