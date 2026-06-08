require 'net/http'

def check_url(url, timeout: 5)
  uri = URI(url)
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = (uri.scheme == 'https')
  http.open_timeout = http.read_timeout = timeout
  res = http.request_head(uri.request_uri)
  { url: url, code: res.code, ok: res.is_a?(Net::HTTPSuccess) }
rescue StandardError => e
  { url: url, ok: false, error: e.message }
end

%w[https://example.com https://invalid.invalid].each { |u| p check_url(u) }
