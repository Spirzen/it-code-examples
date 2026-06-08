module Loggable
  def log(message)
    puts "[#{Time.now}] #{message}"
  end
end

module Retryable
  def with_retry(max: 3)
    yield
  rescue => e
    retry if (max -= 1) > 0
    raise
  end
end

class Downloader
  include Loggable
  include Retryable

  def fetch(url)
    with_retry do
      log("Fetching #{url}")
      Net::HTTP.get(URI(url))  # require 'net/http'; require 'uri'
    end
  end
end
