require 'pg'

conn = PG.connect(
  host: 'localhost',
  dbname: 'myapp_dev',
  user: 'timur',
  password: 'secret'
)

res = conn.exec('SELECT id, name FROM users WHERE active = $1', [true])
res.each do |row|
  puts "ID: #{row['id']}, Name: #{row['name']}"
end
res.clear
conn.close
