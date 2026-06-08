#[async_trait]
pub trait UserRepository {
    async fn find_by_email(&self, email: &str) -> Result<Option<User>, DbErr>;
    async fn save(&self, user: User) -> Result<(), DbErr>;
}

// Реализация для SeaORM
pub struct SeaOrmUserRepository {
    db: DatabaseConnection,
}

// Mock-реализация для тестов
pub struct MockUserRepository {
    users: HashMap<String, User>,
}
