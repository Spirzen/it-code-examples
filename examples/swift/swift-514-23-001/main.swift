enum SortOrder { case newest, oldest }

struct OrderService {
    func fetchOrders(
        for userID: Int,
        status: OrderStatus? = nil,
        sortedBy order: SortOrder = .newest,
        using session: URLSession = .shared
    ) async throws -> [Order] {
        var components = URLComponents(string: "https://api.example.com/users/\(userID)/orders")!
        if let status {
            components.queryItems = [URLQueryItem(name: "status", value: status.rawValue)]
        }
        let url = components.url!
        let (data, response) = try await session.data(from: url)
        guard let http = response as? HTTPURLResponse, (200...299).contains(http.statusCode) else {
            throw OrderError.badResponse
        }
        var orders = try JSONDecoder().decode([Order].self, from: data)
        switch order {
        case .newest: orders.sort { $0.createdAt > $1.createdAt }
        case .oldest: orders.sort { $0.createdAt < $1.createdAt }
        }
        return orders
    }
}
