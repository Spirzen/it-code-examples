job_queue = Queue.new

# Потребитель
worker = Thread.new do
  loop do
    job = job_queue.pop  # блокируется, пока нет задач
    break if job == :stop
    puts "Обрабатываю: #{job}"
    sleep 0.01
  end
end

# Производители
10.times do |i|
  Thread.new { job_queue << "задача-#{i}" }
end

sleep 0.1
job_queue << :stop
worker.join
