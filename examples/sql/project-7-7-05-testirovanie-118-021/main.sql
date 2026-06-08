CREATE OR REPLACE FUNCTION test_get_user_by_id() RETURNS void AS $$
BEGIN
  -- Устанавливаем план тестов (ожидаемое количество проверок)
  SELECT plan(2);

  -- Вызываем тестируемую функцию
  PERFORM get_user_by_id(1);

  -- Проверяем результат
  SELECT is(get_user_by_id(1), 'Ivan', 'User Ivan found');
  SELECT results_eq('SELECT name FROM users WHERE id = 1', ARRAY['Ivan'], 'Name matches expected value');

  -- Завершаем тест
  SELECT done();
END;
$$ LANGUAGE plpgsql;
