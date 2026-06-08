def process_order(params)
  user = find_or_create_user(params)
  order = build_order(user, params)
  apply_discounts(order)
  order.save!
  process_payment(order, params) if params[:payment_method]
  notify_about_order(order)
  order
end

private

def find_or_create_user(params)
  User.find_by(email: params[:email]) ||
    User.create!(
      email: params[:email],
      name: params[:name],
      address: params[:address]
    )
end

def build_order(user, params)
  order = Order.new(user: user, status: :pending)
  add_items_to_order(order, params[:items])
  calculate_totals(order)
  order
end

def add_items_to_order(order, items_params)
  items_params.each do |item_params|
    product = Product.find(item_params[:product_id])
    quantity = item_params[:quantity].to_i
    order.items << OrderItem.new(
      product: product,
      quantity: quantity,
      unit_price: product.price
    )
  end
end

def calculate_totals(order)
  order.total = order.items.sum(&:total_price)
  order.tax = order.total * 0.2
  order.grand_total = order.total + order.tax
end

def apply_discounts(order)
  order.apply_discount(5) if order.grand_total > 1000
end

def process_payment(order, params)
  PaymentService.new.process(order)
end

def notify_about_order(order)
  NotificationService.new.order_created(order)
end
