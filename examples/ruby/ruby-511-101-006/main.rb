# Слишком много позиционных параметров
def create_user(email, password, first_name, last_name, role, status, locale)
  # реализация
end

# Использование именованных параметров
def create_user(email:, password:, first_name:, last_name:, role: :user, status: :active, locale: "en")
  # реализация
end

# Использование объекта параметров
class UserParams
  attr_reader :email, :password, :first_name, :last_name, :role, :status, :locale

  def initialize(params)
    @email = params[:email]
    @password = params[:password]
    # ...
  end
end

def create_user(params)
  validated = UserParams.new(params)
  # реализация
end
