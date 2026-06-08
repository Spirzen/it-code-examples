require 'async'
require 'async/semaphore'
require 'async/http/internet'

Async do
  semaphore = Async::Semaphore.new(5)
  internet = Async::HTTP::Internet.new
  ids = (1..20).to_a

  tasks = ids.map do |id|
    Async do
      semaphore.async do
        response = internet.get("https://api.example.com/users/#{id}")
        puts "user=#{id} status=#{response.status}"
        response.close
      end
    end
  end

  tasks.each(&:wait)
ensure
  internet&.close
end
