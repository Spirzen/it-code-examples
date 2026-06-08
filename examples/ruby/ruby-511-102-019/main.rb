module ActiveRecord
  def self.included(base)
    base.extend(ClassMethods)
  end
  
  module ClassMethods
    def has_many(name)
      log_info("Определена связь has_many: #{name}")
      # Логика создания связи
    end
    
    def belongs_to(name)
      log_info("Определена связь belongs_to: #{name}")
      # Логика создания связи
    end
  end
  
  def save
    log_info("Сохранение записи")
    # Логика сохранения
  end
  
  def destroy
    log_info("Удаление записи")
    # Логика удаления
  end
end

class Post
  include Loggable
  include ActiveRecord
  
  has_many :comments
  belongs_to :author
  
  attr_accessor :title, :content
  
  def initialize(title, content)
    @title = title
    @content = content
  end
end

class Comment
  include Loggable
  include ActiveRecord
  
  belongs_to :post
  belongs_to :author
  
  attr_accessor :body
  
  def initialize(body)
    @body = body
  end
end

# [2026-02-11 12:00:00] INFO: Определена связь has_many: comments
# [2026-02-11 12:00:00] INFO: Определена связь belongs_to: author
# [2026-02-11 12:00:00] INFO: Определена связь belongs_to: post
# [2026-02-11 12:00:00] INFO: Определена связь belongs_to: author

post = Post.new("Заголовок", "Содержание")
post.save
# [2026-02-11 12:00:00] INFO: Сохранение записи

comment = Comment.new("Отличная статья!")
comment.save
# [2026-02-11 12:00:00] INFO: Сохранение записи
