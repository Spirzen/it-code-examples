function Get-FilesOlderThan {
    [CmdletBinding()]
    [OutputType([System.IO.FileInfo[]])]
    param(
        [Parameter(Mandatory)]
        [string]$Path,

        [Parameter(Mandatory)]
        [ValidateRange(1, [int]::MaxValue)]
        [int]$Days
    )

    $cutoff = (Get-Date).AddDays(-$Days)
    Get-ChildItem -LiteralPath $Path -File |
        Where-Object { $_.LastWriteTime -lt $cutoff }
}
