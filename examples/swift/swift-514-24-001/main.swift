enum LoadState {
    case idle
    case loading(progress: Double)
    case loaded(data: Data)
    case failed(message: String)
}

func describe(_ state: LoadState) -> String {
    switch state {
    case .idle:
        return "нет данных"
    case .loading(let progress):
        return String(format: "%.0f%%", progress * 100)
    case .loaded(let data):
        return "получено \(data.count) байт"
    case .failed(let message):
        return message
    }
}
