# Плохой подход — исключение для управления потоком
def find_user(id)
  raise NotFoundError unless users.include?(id)
  users[id]
end

begin
  user = find_user(id)
rescue NotFoundError
  user = create_default_user
end

# Лучший подход — возврат значения или использование опционального типа
def find_user(id)
  users[id]
end

user = find_user(id) || create_default_user
