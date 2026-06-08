class NativeBridge {
    @JavascriptInterface
    fun postMessage(message: String) {
        val json = JSONObject(message)
        val id = json.getInt("id")
        val method = json.getString("method")
        val params = json.getJSONObject("params")

        when (method) {
            "getDeviceInfo" -> handleDeviceInfo(id)
            "shareContent" -> handleShare(id, params)
            "openCamera" -> handleCamera(id, params)
            "getGeolocation" -> handleGeolocation(id)
        }
    }

    private fun handleDeviceInfo(callId: Int) {
        val info = JSONObject().apply {
            put("platform", "android")
            put("version", Build.VERSION.RELEASE)
            put("model", Build.MODEL)
        }
        sendResponse(callId, info)
    }

    private fun sendResponse(callId: Int, result: JSONObject) {
        val response = JSONObject().apply {
            put("id", callId)
            put("result", result)
        }
        val js = "window.bridge.handleResponse('${response}');"
        webView.post { webView.evaluateJavascript(js, null) }
    }
}
