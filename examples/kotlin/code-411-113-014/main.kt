fun exportToPdf(webView: WebView, outputFile: File) {
    val adapter = webView.createPrintDocumentAdapter("document")
    val printManager = context.getSystemService(Context.PRINT_SERVICE) as PrintManager
    val attributes = PrintAttributes.Builder()
        .setMediaSize(PrintAttributes.MediaSize.ISO_A4)
        .setResolution(PrintAttributes.Resolution("pdf", "pdf", 300, 300))
        .setMinMargins(PrintAttributes.Margins.NO_MARGINS)
        .build()

    adapter.onLayout(null, attributes, null, object : PrintDocumentAdapter.LayoutResultCallback() {
        override fun onLayoutFinished(info: PrintDocumentInfo, changed: Boolean) {
            adapter.onWrite(
                arrayOf(PageRange.ALL_PAGES),
                ParcelFileDescriptor.open(outputFile, ParcelFileDescriptor.MODE_CREATE or ParcelFileDescriptor.MODE_WRITE_ONLY),
                attributes,
                object : PrintDocumentAdapter.WriteResultCallback() {
                    override fun onWriteFinished(pages: Array<out PageRange>) {
                        Log.i("PDF", "Export completed: ${outputFile.absolutePath}")
                    }
                }
            )
        }
    }, null)
}
