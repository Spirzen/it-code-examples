describe "#discounted_price" do
  it "returns zero for 100% discount" do
    product = Product.new(price: 100)
    expect(product.discounted_price(100)).to eq(0)
  end

  it "returns original price for 0% discount" do
    product = Product.new(price: 100)
    expect(product.discounted_price(0)).to eq(100)
  end

  it "handles negative discount as zero" do
    product = Product.new(price: 100)
    expect(product.discounted_price(-10)).to eq(100)
  end
end
