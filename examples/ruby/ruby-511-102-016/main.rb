module Loggable
  def log(message)
    timestamp = Time.now.strftime("%Y-%m-%d %H:%M:%S")
    puts "[#{timestamp}] #{message}"
  end
  
  def log_error(error)
    log("ERROR: #{error}")
  end
  
  def log_info(info)
    log("INFO: #{info}")
  end
end

module Validatable
  def validate_presence(field, value)
    unless value && !value.to_s.strip.empty?
      errors << "#{field} не может быть пустым"
    end
  end
  
  def validate_length(field, value, min:, max:)
    length = value.to_s.length
    if length < min
      errors << "#{field} должен быть не менее #{min} символов"
    elsif length > max
      errors << "#{field} должен быть не более #{max} символов"
    end
  end
  
  def errors
    @errors ||= []
  end
  
  def valid?
    errors.empty?
  end
end

module Timestampable
  attr_reader :created_at, :updated_at
  
  def touch
    @updated_at = Time.now
  end
  
  private
  
  def set_timestamps
    @created_at = Time.now
    @updated_at = Time.now
  end
end
