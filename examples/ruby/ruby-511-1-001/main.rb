module Logging
  def greet
    "[log] #{super}"
  end
end

module Greeter
  def greet
    "Hello"
  end
end

class User
  prepend Logging
  include Greeter
end

User.ancestors.take(5)
# => [Logging, User, Greeter, Object, Kernel, ...]

User.new.greet
# => "[log] Hello"   # Logging вызывает super → Greeter
