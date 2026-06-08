class ShoppingCart
  def initialize
    @items = []
  end

  def add_item(product, quantity: 1)
    existing = @items.find { |item| item.product == product }
    if existing
      existing.quantity += quantity
    else
      @items << CartItem.new(product, quantity)
    end
  end

  def total
    @items.sum(&:price)
  end

  private

  attr_reader :items
end
