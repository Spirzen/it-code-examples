class ViewModel: ObservableObject {
    @Published var userName = ""
    
    private var cancellables = Set<AnyCancellable>()
    
    init() {
        $userName
            .debounce(for: .milliseconds(500), scheduler: RunLoop.main)
            .removeDuplicates()
            .sink { name in
                print("Поиск по запросу: \(name)")
            }
            .store(in: &cancellables)
    }
}
