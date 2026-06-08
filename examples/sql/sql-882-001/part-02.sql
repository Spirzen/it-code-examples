CREATE PROCEDURE update_salary
  @emp_id INT,
  @amount DECIMAL(10,2)
AS
BEGIN
  BEGIN TRY
    BEGIN TRANSACTION;
    
    UPDATE employees 
    SET salary = salary + @amount 
    WHERE emp_id = @emp_id;
    
    COMMIT TRANSACTION;
  END TRY
  BEGIN CATCH
    ROLLBACK TRANSACTION;
    THROW;
  END CATCH
END
