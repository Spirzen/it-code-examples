// MARK: - Lifecycle
extension ViewController {
    override func viewDidLoad() { ... }
    override func viewWillAppear(_ animated: Bool) { ... }
}

// MARK: - UITableViewDataSource
extension ViewController: UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int { ... }
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell { ... }
}

// MARK: - Private Helpers
extension ViewController {
    private func configureUI() { ... }
    private func loadData() { ... }
}
