# Нарушение принципа
class UserAndOrderManager
  def create_user(params); end
  def create_order(params); end
  def send_welcome_email(user); end
end

# Соблюдение принципа
class UserManager
  def create(params); end
end

class OrderManager
  def create(params); end
end

class WelcomeEmailService
  def send(user); end
end
