@CompileStatic
class UserRepository {
    private final Sql sql
    
    UserRepository(DataSource dataSource) {
        this.sql = new Sql(dataSource)
    }
    
    List<User> findAllActive() {
        sql.rows('SELECT * FROM users WHERE status = ?', ['ACTIVE'])
            .collect { rowToUser(it) }
    }
    
    User findById(Long id) {
        def row = sql.firstRow('SELECT * FROM users WHERE id = ?', [id])
        row ? rowToUser(row) : null
    }
    
    private User rowToUser(Map row) {
        new User(
            id: row.id as Long,
            email: row.email as String,
            name: row.name as String,
            status: row.status as String,
            createdAt: row.created_at as Timestamp
        )
    }
}
