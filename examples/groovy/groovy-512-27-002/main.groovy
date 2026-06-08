package apitester.model

class HttpResponseResult {

    boolean success
    int statusCode
    long responseTimeMs
    long responseSizeBytes
    String responseBody
    String responseHeaders
    String requestHeaders
    String contentType
    String errorMessage

    static HttpResponseResult error(String message) {
        new HttpResponseResult(
            success: false,
            statusCode: 0,
            responseTimeMs: 0,
            responseSizeBytes: 0,
            errorMessage: message
        )
    }

}
