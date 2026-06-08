require 'rails_helper' # Или 'spec_helper' для чистого Ruby

RSpec.describe User, type: :model do
  describe '#full_name' do
    it 'возвращает полное имя пользователя' do
      user = User.new(first_name: 'Иван', last_name: 'Петров')
      expect(user.full_name).to eq('Иван Петров')
    end

    it 'не должен возвращать пустое имя при отсутствии данных' do
      user = User.new
      expect(user.full_name).to be_empty
    end
  end
end
