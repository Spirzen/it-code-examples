-- Пример подсказок в SQL Server
SELECT 
    c.CustomerName,
    o.OrderDate,
    od.Quantity,
    od.UnitPrice,
    p.ProductName
FROM Customers c WITH (INDEX(IX_Customers_CustomerName))
JOIN Orders o WITH (FORCESEEK) ON c.CustomerID = o.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE o.OrderDate >= DATEADD(MONTH, -6, GETDATE)
  AND c.Country = 'USA'
ORDER BY o.OrderDate DESC
OPTION (HASH JOIN, FAST 1000);
