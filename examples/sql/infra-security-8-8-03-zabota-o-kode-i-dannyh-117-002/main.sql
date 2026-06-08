-- Пример дампа MySQL с командами
DROP DATABASE IF EXISTS company_db;
CREATE DATABASE company_db CHARACTER SET utf8mb4;

USE company_db;

CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    salary DECIMAL(10, 2)
);

INSERT INTO employees VALUES (1, 'Ivan', 50000.00);
INSERT INTO employees VALUES (2, 'Maria', 60000.00);
