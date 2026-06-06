def twice
  2.times { |i| yield i }
end

twice { |n| puts "step #{n}" }
