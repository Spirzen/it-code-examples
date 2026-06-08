class PinnedWebViewClient : WebViewClient() {
    private val expectedHash = "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="

    override fun onReceivedSslError(
        view: WebView,
        handler: SslErrorHandler,
        error: SslError
    ) {
        val certificate = error.certificate
        val publicKey = certificate.publicKey.encoded
        val hash = Base64.encodeToString(
            MessageDigest.getInstance("SHA-256").digest(publicKey),
            Base64.NO_WRAP
        )

        if (hash == expectedHash) {
            handler.proceed()
        } else {
            handler.cancel()
            reportSecurityEvent(error)
        }
    }
}
