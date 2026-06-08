
Разбор:
- Фрагмент показывает конкретный сценарий, который стартует со строки `Разбор:` и задаёт контекст выполнения.
- Ключевые элементы блока: `Thread.new`, `join`, `Mutex`, `Queue`, `ConditionVariable`, они определяют основную логику примера.
- По шагам код выполняется так: `Разбор:` -> `- Фрагмент показывает конкретный сценарий, который стартует со строк` -> `- Ключевые элементы блока: `Thread.new`, `join`, `Queue`, они опреде` -> `- По шагам код выполняется так: `job_queue = Queue.new` -> `# Потреб`.
- Для корректности важно поведение конкурентности: где блокировка, где ожидание, и как исключаются гонки между задачами.
- Типичная ошибка при развитии такого кода — смешивать бизнес-правила и инфраструктурные детали в одном месте; лучше разделять ответственность.

mutex = Mutex.new
cv = ConditionVariable.new
items = []

producer = Thread.new do
  5.times do |i|
    mutex.synchronize do
      items << "элемент-#{i}"
      cv.signal  # будит один ожидающий поток
    end
    sleep 0.05
  end
end

consumer = Thread.new do
  5.times do
    mutex.synchronize do
      # Ждём, пока items не станет непустым
      cv.wait(mutex) while items.empty?
      puts "Получил: #{items.shift}"
    end
  end
end

producer.join
consumer.join
