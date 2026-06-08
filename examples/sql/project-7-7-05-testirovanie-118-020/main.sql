CREATE PROCEDURE TestSchema.Test_AddUser
AS
BEGIN
    -- Создаем фейковую таблицу пользователей
    EXEC tSQLt.FakeTable 'Users';
    
    -- Вставляем тестовые данные
    INSERT INTO Users (Id, Name) VALUES (1, 'Ivan');
    
    -- Вызываем тестируемую логику (предположим, есть процедура AddUser)
    EXEC dbo.AddUser @Name = 'Maria';
    
    -- Проверяем результат
    DECLARE @ExpectedCount INT = 2;
    DECLARE @ActualCount INT;
    
    SELECT @ActualCount = COUNT(*) FROM Users;
    
    EXEC tSQLt.AssertEquals @ExpectedCount, @ActualCount;
END;
