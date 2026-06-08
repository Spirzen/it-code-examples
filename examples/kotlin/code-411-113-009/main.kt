class WebViewPreloader(private val context: Context) {
    private var cachedWebView: WebView? = null

    fun preload() {
        CoroutineScope(Dispatchers.Main).launch {
            cachedWebView = WebView(context.applicationContext).apply {
                settings.javaScriptEnabled = true
                settings.domStorageEnabled = true
            }
            cachedWebView?.loadUrl("about:blank")
        }
    }

    fun obtain(): WebView {
        return cachedWebView ?: WebView(context)
    }

    fun destroy() {
        cachedWebView?.destroy()
        cachedWebView = null
    }
}
