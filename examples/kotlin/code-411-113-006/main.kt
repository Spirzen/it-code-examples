webView.setWebViewAssetLoader(
    WebViewAssetLoader.Builder()
        .setDomain("app.example.com")
        .addPathHandler(
            "/assets/",
            WebViewAssetLoader.AssetsPathHandler(context)
        )
        .addPathHandler(
            "/internal/",
            WebViewAssetLoader.InternalStoragePathHandler(
                context,
                File(context.filesDir, "www")
            )
        )
        .build()
)

webView.webViewClient = object : WebViewClient() {
    override fun shouldInterceptRequest(
        view: WebView,
        request: WebResourceRequest
    ): WebResourceResponse? {
        return assetLoader.shouldInterceptRequest(request.url)
    }
}

webView.loadUrl("https://app.example.com/assets/index.html")
