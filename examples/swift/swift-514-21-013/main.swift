import SwiftUI

struct FeedView: View {
    @Environment(\.scenePhase) private var scenePhase
    @State private var refreshTask: Task<Void, Never>?

    var body: some View {
        List { Text("Лента") }
            .onChange(of: scenePhase) { _, phase in
                switch phase {
                case .active:
                    refreshTask = Task { await loadFeed() }
                case .background, .inactive:
                    refreshTask?.cancel()
                @unknown default:
                    break
                }
            }
    }

    func loadFeed() async { /* сеть */ }
}
