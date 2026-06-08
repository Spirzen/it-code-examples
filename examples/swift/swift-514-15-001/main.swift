import UIKit

final class CounterViewController: UIViewController {
    private let label = UILabel()
    private var count = 0

    override func viewDidLoad() {
        super.viewDidLoad()
        let button = UIButton(type: .system)
        button.setTitle("Увеличить", for: .normal)
        button.addTarget(self, action: #selector(increment), for: .touchUpInside)
        // размещение label и button через Auto Layout опущено
    }

    @objc private func increment() {
        count += 1
        label.text = "Счёт: \(count)"
    }
}
