// schema.rs (генерируется)
table! {
    users (id) {
        id -> Integer,
        name -> Text,
        email -> Text,
    }
}

// models.rs
#[derive(Queryable)]
pub struct User {
    pub id: i32,
    pub name: String,
    pub email: String,
}

// Использование
use diesel::prelude::*;
use crate::schema::users;

fn find_user_by_email(conn: &mut PgConnection, email: &str) -> QueryResult<User> {
    users::table
        .filter(users::email.eq(email))
        .first(conn)
}
