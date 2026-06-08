CREATE PROCEDURE transfer_funds(
    IN from_account INT,
    IN to_account INT,
    IN amount DECIMAL,
    OUT status TEXT
)
AS $$
BEGIN
    -- Логика перевода
    UPDATE accounts SET balance = balance - amount WHERE id = from_account;
    UPDATE accounts SET balance = balance + amount WHERE id = to_account;
    status := 'OK';
END;
$$ LANGUAGE plpgsql;
