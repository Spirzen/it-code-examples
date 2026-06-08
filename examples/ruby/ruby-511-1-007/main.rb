class FlexibleHash
  def initialize
    @store = {}
  end

  def method_missing(name, *args, &block)
    if name.to_s.end_with?('=')
      key = name.to_s[0..-2].to_sym
      @store[key] = args.first
    else
      @store[name]
    end
  end

  def respond_to_missing?(name, _include_private = false)
    name.to_s.end_with?('=') || @store.key?(name.to_sym)
  end
end

h = FlexibleHash.new
h.name = "Ruby"
h.name  # => "Ruby"
