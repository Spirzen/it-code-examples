[System.Collections.ArrayList]$systemInfo = @()
$os = Get-WmiObject Win32_OperatingSystem
$cpu = Get-WmiObject Win32_Processor
$memory = Get-WmiObject Win32_PhysicalMemory

foreach ($mem in $memory) {
    $systemInfo.Add([PSCustomObject]@{
        Component = "RAM"
        SizeGB = [math]::Round($mem.Capacity / 1GB, 2)
        Manufacturer = $mem.Manufacturer
    }) | Out-Null
}

foreach ($proc in $cpu) {
    $systemInfo.Add([PSCustomObject]@{
        Component = "CPU"
        Model = $proc.Name
        Cores = $proc.NumberOfCores
        Threads = $proc.NumberOfLogicalProcessors
    }) | Out-Null
}

$systemInfo | Format-Table -AutoSize
