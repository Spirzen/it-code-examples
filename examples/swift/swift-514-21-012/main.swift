final class OrdersViewController: UIViewController {
    private var refreshTask: Task<Void, Never>?

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        refreshTask = Task { await reloadOrders() }
    }

    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        refreshTask?.cancel()
    }

    @MainActor
    private func reloadOrders() async {
        // загрузка и обновление UI
    }
}
