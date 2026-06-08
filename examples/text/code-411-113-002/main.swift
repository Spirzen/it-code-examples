
import WebKit

class WebContainerViewController: UIViewController {
    private var webView: WKWebView!
    private var configuration: WKWebViewConfiguration!

    override func viewDidLoad() {
        super.viewDidLoad()
        setupWebView()
        loadContent()
    }

    private func setupWebView() {
        configuration = WKWebViewConfiguration()
        configuration.preferences.javaScriptEnabled = true
        configuration.websiteDataStore = WKWebsiteDataStore.default()

        let userScript = WKUserScript(
            source: bridgeScript(),
            injectionTime: .atDocumentStart,
            forMainFrameOnly: true
        )
        configuration.userContentController.addUserScript(userScript)
        configuration.userContentController.add(self, name: "nativeBridge")

        webView = WKWebView(frame: view.bounds, configuration: configuration)
        webView.navigationDelegate = self
        webView.uiDelegate = self
        view.addSubview(webView)
    }

    private func loadContent() {
        let url = URL(string: "https://example.com")!
        let request = URLRequest(url: url)
        webView.load(request)
    }

    private func bridgeScript() -> String {
        return """
        window.NativeBridge = {
            call: function(method, params) {
                window.webkit.messageHandlers.nativeBridge.postMessage({
                    method: method,
                    params: params
                });
            }
        };
        """
    }
}

extension WebContainerViewController: WKScriptMessageHandler {
    func userContentController(
        _ userContentController: WKUserContentController,
        didReceive message: WKScriptMessage
    ) {
        guard let body = message.body as? [String: Any],
              let method = body["method"] as? String else { return }
        handleNativeCall(method: method, params: body["params"])
    }
}
