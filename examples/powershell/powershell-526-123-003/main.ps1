# Работа с XML
$xmlData = @"
<Root>
    <Item id="1">Text</Item>
</Root>
"@
$xml = [xml]$xmlData
$item = $xml.Root.Item
Write-Host $item.Id

# Работа с JSON
$jsonString = '{"Name": "Test", "Value": 123}'
$jsonObj = $jsonString | ConvertFrom-Json
Write-Host $jsonObj.Name
