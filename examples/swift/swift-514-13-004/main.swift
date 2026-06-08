enum LoadState {
    case idle
    case loading
    case success(data: String)
    case failure(message: String)
}

func render(_ state: LoadState) {
    switch state {
    case .idle:
        print("Ожидание")
    case .loading:
        print("Загрузка…")
    case .success(let data):
        print("Данные: \(data)")
    case .failure(let message):
        print("Ошибка: \(message)")
    }
}
