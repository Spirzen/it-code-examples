// Фейк репозитория пользователей (вместо реальной БД)
class FakeUserRepository {
  constructor() {
    this.users = [];  // просто массив в памяти
  }
  
  add(user) {
    this.users.push(user);
  }
  
  findById(id) {
    return this.users.find(u => u.id === id);
  }
  
  delete(id) {
    this.users = this.users.filter(u => u.id !== id);
  }
}

// В тесте используем фейк, а не реальную БД
const repo = new FakeUserRepository();
const service = new UserService(repo);

service.register({ id: 1, name: 'Вася' });
const user = service.getUser(1);

assert(user.name === 'Вася');  // Всё работает как с настоящей БД
