RSpec.describe Order do
  describe "#total" do
    context "with multiple items" do
      it "sums prices of all items" do
        order = Order.new
        order.add_item(Product.new(price: 100), quantity: 2)
        order.add_item(Product.new(price: 50), quantity: 1)

        expect(order.total).to eq(250)
      end
    end

    context "with discounts" do
      it "applies percentage discount correctly" do
        order = Order.new(discount_percent: 10)
        order.add_item(Product.new(price: 100), quantity: 1)

        expect(order.total).to eq(90)
      end
    end
  end
end
