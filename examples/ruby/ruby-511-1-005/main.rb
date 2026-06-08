def f
  proc { return "from proc" }.call
  "after proc"
end

def g
  lambda { return "from lambda" }.call
  "after lambda"
end

def h
  yield
  "after yield"
end

p f   # => "from proc"
p g   # => "after lambda"
p h { return "from block" }  # LocalJumpError: unexpected return
