class HTTPClient
  def method_missing(verb, path = nil, &block)
    verb = verb.to_s.upcase
    case verb
    when 'GET', 'POST', 'PUT', 'DELETE'
      request = { method: verb, path: path }
      block&.call(request) if block
      perform(request)
    else
      super
    end
  end

  def respond_to_missing?(name, _)
    %w[get post put delete].include?(name.to_s)
  end

  private

  def perform(req)
    puts "→ #{req[:method]} #{req[:path]} (body: #{req[:body]})"
  end
end

client = HTTPClient.new
client.get '/users'
client.post('/posts') { |r| r[:body] = { title: 'Hello' }.to_json }
