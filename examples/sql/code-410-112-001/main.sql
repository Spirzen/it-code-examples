CREATE TABLE Users (
    Id INT PRIMARY KEY IDENTITY(1,1),  -- Автоинкрементный первичный ключ
    Name NVARCHAR(100) NOT NULL,       -- Имя пользователя
    Address NVARCHAR(200) NULL,        -- Адрес (может быть NULL)
    Email NVARCHAR(100) NOT NULL       -- Email (уникальный)
);

