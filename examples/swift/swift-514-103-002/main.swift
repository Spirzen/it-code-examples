
import Foundation

let url = URL(string: "https://example.com")!
let task = URLSession.shared.dataTask(with: url) { data, response, error in
    if let error = error { print(error); return }
    if let http = response as? HTTPURLResponse {
        print("status:", http.statusCode)
    }
    if let data = data, let body = String(data: data, encoding: .utf8) {
        print(body.prefix(200))
    }
}
task.resume()
RunLoop.main.run(until: Date(timeIntervalSinceNow: 1))
