class UserRepositoryTest {
    companion object {
        @Container
        val postgres = PostgreSQLContainer<Nothing>("postgres:15")
            .apply { start() }
    }

    private lateinit var db: Database

    @BeforeEach
    fun setup() {
        db = Database.connect(
            url = postgres.jdbcUrl,
            driver = "org.postgresql.Driver",
            user = postgres.username,
            password = postgres.password
        )
        // Выполнить миграции...
    }

    @Test
    fun `сохранение и выборка`() {
        transaction(db) {
            User.new { name = "Тест" }
        }

        val count = transaction(db) {
            Users.selectAll().count()
        }

        assertEquals(1, count)
    }
}
