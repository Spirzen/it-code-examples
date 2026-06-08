
Разбор:
- Фрагмент показывает конкретный сценарий, который стартует со строки `Это критически важно для:` и задаёт контекст выполнения.
- Ключевые элементы блока: `scope`, `enum`, они определяют основную логику примера.
- По шагам код выполняется так: `Это критически важно для:` -> `- инвалидации кэшей (например, `Rails.cache.fetch("post/#{post.id}")` -> `- сортировки по времени последней активности;` -> `- интеграций, отслеживающих изменения через `updated_at`.`.
- Практически важно добавить обработку ошибок и явные проверки входа, чтобы исключить скрытые падения в рантайме.
- Типичная ошибка при развитии такого кода — смешивать бизнес-правила и инфраструктурные детали в одном месте; лучше разделять ответственность.

class MoneyType < ActiveRecord::Type::Value
  def cast(value)
    return value if value.is_a?(Money)
    Money.new(value.to_i)
  end

  def serialize(value)
    value.cents
  end

  def deserialize(value)
    Money.new(value.to_i)
  end
end

ActiveRecord::Type.register(:money, MoneyType)

class Product < ActiveRecord::Base
  attribute :price, :money
end
