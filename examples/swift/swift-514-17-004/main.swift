func temperatureUpdates() -> AsyncStream<Double> {
    return AsyncStream { continuation in
        let timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { _ in
            let temp = readCurrentTemperature()
            continuation.yield(temp)
        }
        continuation.onTermination = { _ in
            timer.invalidate()
        }
    }
}

// Использование
for await temperature in temperatureUpdates() {
    print("Текущая температура: \(temperature)")
}
