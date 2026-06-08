class LazyAPI
  def method_missing(name, *args)
    return super unless name.to_s.start_with?('fetch_')
    define_singleton_method(name) do |*inner_args|
      # тяжёлая логика: HTTP-запрос, кэш и т.п.
      "result of #{name}(#{inner_args})"
    end
    send(name, *args)
  end

  def respond_to_missing?(name, _)
    name.to_s.start_with?('fetch_') || super
  end
end
