module ClassMethods
  def find_by_id(id)
    log_info("Поиск по ID: #{id}")
    # Логика поиска
  end
  
  def all
    log_info("Получение всех записей")
    # Логика получения всех записей
  end
  
  def count
    log_info("Подсчет записей")
    # Логика подсчета
  end
end

class Product
  extend ClassMethods
  include Loggable
  
  attr_accessor :name, :price
  
  def initialize(name, price)
    @name = name
    @price = price
    log_info("Создан продукт: #{name}")
  end
  
  def self.log_info(message)
    puts "[CLASS] #{message}"
  end
end

Product.find_by_id(1)
# [CLASS] Поиск по ID — 1

Product.all
# [CLASS] Получение всех записей

Product.count
# [CLASS] Подсчет записей

product = Product.new("Книга", 500)
# [2026-02-11 12:00:00] INFO: Создан продукт: Книга
