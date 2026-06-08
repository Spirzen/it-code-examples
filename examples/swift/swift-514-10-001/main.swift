
import SwiftUI

struct ContentView: View {
    @State private var counter = 0

    var body: some View {
        VStack {
            Text("Счётчик: \(counter)")
                .font(.title)
            Button("Увеличить") {
                counter += 1
            }
        }
        .padding()
    }
}
