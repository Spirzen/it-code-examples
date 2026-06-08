CREATE OR REPLACE PROCEDURE update_salary(
  p_emp_id IN NUMBER,
  p_amount IN NUMBER
) AS
BEGIN
  UPDATE employees 
  SET salary = salary + p_amount 
  WHERE emp_id = p_emp_id;
  COMMIT;
EXCEPTION
  WHEN OTHERS THEN
    ROLLBACK;
    RAISE;
END;
