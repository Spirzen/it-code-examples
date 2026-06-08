func applyCustomStyles() {
    let css = """
    body { background-color: #1a1a1a !important; color: #ffffff !important; }
    .header { display: none !important; }
    .content { padding: 16px !important; }
    a { color: #4a9eff !important; }
    """
    let js = """
    var style = document.createElement('style');
    style.textContent = `\(css)`;
    document.head.appendChild(style);
    """
    webView.evaluateJavaScript(js, completionHandler: nil)
}
