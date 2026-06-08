def calculate(a, b, op)
  case op
  when '+' then a + b
  when '-' then a - b
  when '*' then a * b
  when '/'
    raise ArgumentError, 'деление на ноль' if b.zero?
    a / b
  else
    raise ArgumentError, "неизвестная операция: #{op}"
  end
end

loop do
  print 'Операция (+ - * / q): '
  op = gets&.strip
  break if op == 'q'

  a = Float(gets.strip) rescue (puts 'число?'; next)
  b = Float(gets.strip) rescue (puts 'число?'; next)

  begin
    puts "= #{calculate(a, b, op)}"
  rescue ArgumentError => e
    puts e.message
  end
end
