struct Item {
    let name: String
    let price: Int
    let isAvailable: Bool
}

func checkoutTotal(items: [Item], limit: Int) -> Int {
    var total = 0
    for item in items {
        guard item.isAvailable, item.price > 0 else { continue }
        total += item.price
        if total > limit {
            break
        }
    }
    return total
}
