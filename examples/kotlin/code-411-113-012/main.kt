class CustomSchemeHandler : WebViewClient() {
    override fun shouldOverrideUrlLoading(
        view: WebView,
        request: WebResourceRequest
    ): Boolean {
        val uri = request.url
        return when (uri.scheme) {
            "myapp" -> handleCustomScheme(uri)
            "tel" -> openDialer(uri)
            "mailto" -> openEmailClient(uri)
            "intent" -> resolveAndroidIntent(uri)
            else -> false
        }
    }

    private fun handleCustomScheme(uri: Uri): Boolean {
        when (uri.host) {
            "profile" -> navigateToProfile(uri.getQueryParameter("id"))
            "product" -> navigateToProduct(uri.getQueryParameter("sku"))
            "checkout" -> startCheckoutFlow()
        }
        return true
    }
}
