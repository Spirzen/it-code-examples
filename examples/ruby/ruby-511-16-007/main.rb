
Разбор:
- Фрагмент показывает конкретный сценарий, который стартует со строки `Внутри `change` — идемпотентные операции. При выполнении `rails db:migrate`:` и задаёт контекст выполнения.
- Ключевые элементы блока: `change`, `rails`, `db:migrate`, `ActiveRecord`, `schema_migrations`, они определяют основную логику примера.
- По шагам код выполняется так: `Внутри `change` — идемпотентные операции. При выполнении `rails db:m` -> `1. ActiveRecord читает таблицу `schema_migrations`;` -> `2. Находит неприменённые миграции (по версии времени);` -> `3. Выполняет `change` в транзакции (если СУБД это поддерживает);`.
- Практически важно добавить обработку ошибок и явные проверки входа, чтобы исключить скрытые падения в рантайме.
- Типичная ошибка при развитии такого кода — смешивать бизнес-правила и инфраструктурные детали в одном месте; лучше разделять ответственность.

class User < ActiveRecord::Base
  before_save :normalize_email
  validates :email, presence: true, uniqueness: true, format: { with: URI::MailTo::EMAIL_REGEXP }

  private

  def normalize_email
    return if email.nil? || email.empty?
    self.email = email.downcase.strip
  end
end
