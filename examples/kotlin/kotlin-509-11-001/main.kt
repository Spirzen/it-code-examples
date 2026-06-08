  // common
  expect class HttpClient() {
      fun request(url: String): String
  }

  // jvmMain
  actual class HttpClient {
      actual fun request(url: String): String = java.net.URL(url).readText()
  }

  // iosMain
  actual class HttpClient {
      actual fun request(url: String): String = NSURLConnection.sendSynchronousRequest(...)
  }
