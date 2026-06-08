// CalculateDiscount вычисляет скидку на основе суммы заказа.
// Возвращает процент скидки в диапазоне 0-25.
func CalculateDiscount(orderTotal float64) float64 {
    switch {
    case orderTotal >= 1000:
        return 25.0
    case orderTotal >= 500:
        return 15.0
    case orderTotal >= 200:
        return 10.0
    case orderTotal >= 100:
        return 5.0
    default:
        return 0.0
    }
}
