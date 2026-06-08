def process_order(params)
  user = User.find_by(email: params[:email])
  if user.nil?
    user = User.create!(
      email: params[:email],
      name: params[:name],
      address: params[:address]
    )
  end

  order = Order.new
  order.user = user
  order.status = :pending

  total = 0
  params[:items].each do |item_params|
    product = Product.find(item_params[:product_id])
    quantity = item_params[:quantity].to_i
    item_total = product.price * quantity
    total += item_total

    order.items << OrderItem.new(
      product: product,
      quantity: quantity,
      unit_price: product.price
    )
  end

  order.total = total
  order.tax = total * 0.2
  order.grand_total = order.total + order.tax

  if order.grand_total > 1000
    order.apply_discount(5)
  end

  order.save!

  PaymentService.new.process(order) if params[:payment_method]

  NotificationService.new.order_created(order)

  order
end
