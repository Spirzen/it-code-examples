-- PostgreSQL ≥11
CREATE PROCEDURE transfer_funds(from_acc INT, to_acc INT, amount NUMERIC)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE accounts SET balance = balance - amount WHERE id = from_acc;
    UPDATE accounts SET balance = balance + amount WHERE id = to_acc;
    COMMIT;  -- разрешено только в PROCEDURE (не в FUNCTION!)
END;
$$;
CALL transfer_funds(1, 2, 100.00);

-- T-SQL
CREATE PROCEDURE TransferFunds
    @from_acc INT,
    @to_acc INT,
    @amount DECIMAL(18,2)
AS
BEGIN
    BEGIN TRANSACTION;
    UPDATE Accounts SET Balance -= @amount WHERE Id = @from_acc;
    UPDATE Accounts SET Balance += @amount WHERE Id = @to_acc;
    COMMIT;
END;
EXEC TransferFunds 1, 2, 100.00;
