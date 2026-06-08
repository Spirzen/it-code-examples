const c = @cImport({
    @cInclude("curl/curl.h");
});

pub fn main() !void {
    _ = c.curl_global_init(c.CURL_GLOBAL_DEFAULT);
    defer c.curl_global_cleanup();

    const curl = c.curl_easy_init();
    if (curl) |handle| {
        _ = c.curl_easy_setopt(handle, c.CURLOPT_URL, "https://example.com");
        _ = c.curl_easy_perform(handle);
        c.curl_easy_cleanup(handle);
    }
}
