module Loggable
  def logger
    @logger ||= Logger.new($stdout)
  end

  def log(message)
    logger.info "[#{self.class}] #{message}"
  end
end

class PaymentService
  include Loggable

  def process(order)
    log "Processing payment for order ##{order.id}"
    # реализация
  end
end
