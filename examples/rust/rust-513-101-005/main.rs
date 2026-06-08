trait Database {
    fn query(&self, sql: &str) -> Result<Vec<Row>, DbError>;
}

struct RealDatabase { /* ... */ }
impl Database for RealDatabase { /* ... */ }

#[cfg(test)]
struct MockDatabase {
    responses: HashMap<String, Result<Vec<Row>, DbError>>,
}

#[cfg(test)]
impl Database for MockDatabase {
    fn query(&self, sql: &str) -> Result<Vec<Row>, DbError> {
        self.responses.get(sql).cloned().unwrap_or_else(|| 
            Err(DbError::QueryFailed)
        )
    }
}
