function Stop-ServiceWithTimeout {
    param(
        [string]$Name,
        [int]$TimeoutSec = 120
    )

    Stop-Service -Name $Name -NoWait -ErrorAction Stop

    $sw = [Diagnostics.Stopwatch]::StartNew()
    while ((Get-Service -Name $Name).Status -ne 'Stopped') {
        if ($sw.Elapsed.TotalSeconds -ge $TimeoutSec) {
            throw "Служба $Name не остановилась за $TimeoutSec с."
        }
        Start-Sleep -Seconds 2
    }
}
