
import Charts

struct SalesChart: View {
    let salesData: [(String, Int)] = [("Янв", 120), ("Фев", 190), ("Мар", 150)]

    var body: some View {
        Chart(salesData, id: \.0) { month, value in
            BarMark(
                x: .value("Месяц", month),
                y: .value("Продажи", value)
            )
        }
        .frame(height: 200)
    }
}
