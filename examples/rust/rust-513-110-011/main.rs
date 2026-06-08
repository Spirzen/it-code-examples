use mockall::*;

#[automock]
trait Database {
    fn get_user(&self, id: u32) -> Option<String>;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_with_mock() {
        let mut mock = MockDatabase::new();
        mock.expect_get_user()
            .with(eq(42))
            .returning(|_| Some("Алексей".to_string()));

        assert_eq!(mock.get_user(42), Some("Алексей".to_string()));
    }
}
