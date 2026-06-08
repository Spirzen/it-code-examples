# app/services/order_fulfillment_service.rb
class OrderFulfillmentService
  def initialize(order)
    @order = order
  end

  def fulfill!
    return false unless order.can_be_fulfilled?

    ActiveRecord::Base.transaction do
      reserve_inventory
      charge_customer
      schedule_shipping
      update_order_status
      send_fulfillment_notification
    end

    true
  rescue InventoryUnavailableError => e
    handle_inventory_error(e)
    false
  rescue PaymentDeclinedError => e
    handle_payment_error(e)
    false
  end

  private

  attr_reader :order

  def reserve_inventory
    order.items.each do |item|
      Inventory.reserve(item.product_id, item.quantity)
    end
  end

  def charge_customer
    payment = PaymentProcessor.charge(
      customer: order.customer,
      amount: order.total,
      description: "Order ##{order.id}"
    )
    order.update!(payment_id: payment.id)
  end

  # остальные приватные методы...
end

# Использование в контроллере
class OrdersController < ApplicationController
  def fulfill
    order = Order.find(params[:id])
    service = OrderFulfillmentService.new(order)

    if service.fulfill!
      redirect_to order, notice: "Order fulfilled successfully"
    else
      redirect_to order, alert: "Failed to fulfill order"
    end
  end
end
