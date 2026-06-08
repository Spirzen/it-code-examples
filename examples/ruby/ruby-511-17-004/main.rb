require 'eventmachine'

class HttpClient < EM::Connection
  def post_init
    send_data "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n"
  end

  def receive_data(data)
    @buffer ||= ""
    @buffer << data
  end

  def unbind
    puts "Получен ответ (#{[@buffer.bytesize]} байт)"
    EM.stop
  end
end

EM.run do
  EM.connect "example.com", 80, HttpClient
end
