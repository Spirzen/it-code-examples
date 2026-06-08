# Числа как объекты
5.class          # Integer
5.even?          # true
5.odd?           # false
5.times { puts "Hello" }

# Строки как объекты
"hello".class    # String
"hello".upcase   # "HELLO"
"hello".length   # 5
"hello".reverse  # "olleh"

# Символы как объекты
:hello.class     # Symbol
:hello.to_s      # "hello"
:hello.inspect   # ":hello"

# Классы как объекты
String.class     # Class
Array.class      # Class
Class.class      # Class

# Даже nil является объектом
nil.class        # NilClass
nil.nil?         # true
nil.to_s         # ""
