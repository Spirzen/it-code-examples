require 'json'

DB = 'tasks.json'

def load_tasks
  return [] unless File.exist?(DB)
  JSON.parse(File.read(DB, encoding: 'UTF-8'))
rescue JSON::ParserError
  []
end

def save_tasks(tasks)
  File.write(DB, JSON.pretty_generate(tasks), encoding: 'UTF-8')
end

def add_task(title)
  tasks = load_tasks
  tasks << { id: Time.now.to_i, title: title, done: false }
  save_tasks(tasks)
end

def toggle(id)
  tasks = load_tasks
  task = tasks.find { |t| t['id'] == id }
  return warn('нет задачи') unless task
  task['done'] = !task['done']
  save_tasks(tasks)
end

add_task('Изучить Ruby')
load_tasks.each { |t| puts "[#{t['done'] ? 'x' : ' '}] #{t['title']}" }
