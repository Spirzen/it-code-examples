webView.settings.apply {
    // Отключение доступа к файловой системе
    allowFileAccess = false
    allowContentAccess = false
    allowFileAccessFromFileURLs = false
    allowUniversalAccessFromFileURLs = false

    // Ограничение JavaScript
    javaScriptEnabled = true
    javaScriptCanOpenWindowsAutomatically = false

    // Смешанный контент запрещён
    mixedContentMode = WebSettings.MIXED_CONTENT_NEVER_ALLOW

    // Отключение отладки в production
    WebView.setWebContentsDebuggingEnabled(BuildConfig.DEBUG)

    // Безопасное отображение
    safeBrowsingEnabled = true
}
