# Пример кода в стиле Rails, демонстрирующий ООП концепции
class Post < ApplicationRecord
  belongs_to :author
  has_many :comments
  has_many :tags, through: :post_tags
  
  validates :title, presence: true, length: { minimum: 5 }
  validates :content, presence: true
  
  scope :published, -> { where(published: true) }
  scope :recent, -> { order(created_at: :desc) }
  
  def publish!
    update(published: true, published_at: Time.now)
  end
  
  def to_param
    "#{id}-#{title.parameterize}"
  end
end

# Использование полиморфизма в коллекциях
posts = Post.published.recent.limit(10)
posts.each do |post|
  puts "#{post.title} by #{post.author.name}"
  puts "Comments: #{post.comments.count}"
end
