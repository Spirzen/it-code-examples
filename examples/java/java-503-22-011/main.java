   @Testcontainers
   class UserRepositoryTest {
       @Container
       static PostgreSQLContainer<?> postgres = 
           new PostgreSQLContainer<>("postgres:15");

       @DynamicPropertySource
       static void configureProperties(DynamicPropertyRegistry registry) {
           registry.add("spring.datasource.url", postgres::getJdbcUrl);
           registry.add("spring.datasource.username", postgres::getUsername);
           registry.add("spring.datasource.password", postgres::getPassword);
       }

       @Test
       void shouldFindUserByEmail() { ... }
   }
