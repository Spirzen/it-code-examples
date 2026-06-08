#[derive(Serialize)]
pub struct UserResponse {
    id: i32,
    name: String,
    email: String,
    created_at: chrono::DateTime<Utc>,
}

impl From<User> for UserResponse {
    fn from(user: User) -> Self {
        Self {
            id: user.id,
            name: user.name,
            email: user.email,
            created_at: Utc::now(), // или из базы
        }
    }
}
