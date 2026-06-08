CREATE DATABASE shop;
USE shop;

CREATE TABLE accounts (
  id INT PRIMARY KEY,
  balance DECIMAL NOT NULL CHECK (balance >= 0)
);

INSERT INTO accounts VALUES (1, 1000), (2, 500);

BEGIN;
  UPDATE accounts SET balance = balance - 100 WHERE id = 1;
  UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

SELECT * FROM accounts;
