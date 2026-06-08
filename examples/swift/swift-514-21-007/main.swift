class DataViewController: UIViewController {
    
    private var dataManager: DataManager?
    private var observers: [NSObjectProtocol] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        dataManager = DataManager.shared
        setupObservers()
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        dataManager?.startFetching()
    }
    
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        dataManager?.stopFetching()
    }
    
    override func viewDidDisappear(_ animated: Bool) {
        super.viewDidDisappear(animated)
        removeObservers()
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        dataManager?.clearCache()
    }
    
    private func setupObservers() {
        let notificationCenter = NotificationCenter.default
        
        let observer1 = notificationCenter.addObserver(
            forName: .dataUpdated,
            object: nil,
            queue: .main
        ) { [weak self] notification in
            self?.handleDataUpdate()
        }
        observers.append(observer1)
        
        let observer2 = notificationCenter.addObserver(
            forName: .connectionChanged,
            object: nil,
            queue: .main
        ) { [weak self] notification in
            self?.handleConnectionChange()
        }
        observers.append(observer2)
    }
    
    private func removeObservers() {
        let notificationCenter = NotificationCenter.default
        observers.forEach { notificationCenter.removeObserver($0) }
        observers.removeAll()
    }
    
    deinit {
        print("ViewController освобожден")
        removeObservers()
    }
}
