<?php
$pdo = new PDO("sqlsrv:Server=localhost,1433;Database=app_db", "app_user", "secret");
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$pdo->exec("
IF OBJECT_ID('dbo.Users','U') IS NULL
CREATE TABLE dbo.Users(
    Id BIGINT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(255) NOT NULL
)");

$stmt = $pdo->prepare("INSERT INTO dbo.Users(Name) VALUES (:name)");
$stmt->execute([':name' => 'Anna']);

$rows = $pdo->query("SELECT Id, Name FROM dbo.Users")->fetchAll(PDO::FETCH_ASSOC);
foreach ($rows as $row) {
    echo $row['Id'] . " " . $row['Name'] . PHP_EOL;
}
