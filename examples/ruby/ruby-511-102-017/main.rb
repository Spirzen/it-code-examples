class User
  include Loggable
  include Validatable
  
  attr_accessor :username, :email, :password
  
  def initialize(username, email, password)
    @username = username
    @email = email
    @password = password
    log_info("Создан новый пользователь: #{username}")
  end
  
  def validate
    errors.clear
    validate_presence(:username, username)
    validate_presence(:email, email)
    validate_presence(:password, password)
    validate_length(:username, username, min: 3, max: 20)
    validate_length(:password, password, min: 6, max: 100)
    valid?
  end
  
  def save
    if validate
      log_info("Пользователь #{username} сохранен")
      true
    else
      log_error("Ошибка валидации для #{username}: #{errors.join(', ')}")
      false
    end
  end
end

user = User.new("john_doe", "john@example.com", "secret123")
user.save
# [2026-02-11 12:00:00] INFO: Создан новый пользователь: john_doe
# [2026-02-11 12:00:00] INFO: Пользователь john_doe сохранен

invalid_user = User.new("", "", "123")
invalid_user.save
# [2026-02-11 12:00:00] INFO: Создан новый пользователь: 
# [2026-02-11 12:00:00] ERROR: Ошибка валидации для : username не может быть пустым, email не может быть пустым, username должен быть не менее 3 символов, password должен быть не менее 6 символов
