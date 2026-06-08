module Timestampable
  def self.included(base)
    base.extend(ClassMethods)
  end

  module ClassMethods
    def created_at_field(name)
      define_method(name) { Time.now }
    end
  end
end

class Event
  include Timestampable
  created_at_field :logged_at
end

Event.new.logged_at  # => 2025-11-06 12:34:56 +0300
