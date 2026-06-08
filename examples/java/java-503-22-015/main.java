
import org.hibernate.cfg.Configuration;

import jakarta.persistence.EntityManagerFactory;

public class JpaConfig {
    public static EntityManagerFactory createEntityManagerFactory() {
        return new Configuration()
            .addAnnotatedClass(Book.class)
            .setProperty("hibernate.dialect", "org.hibernate.dialect.PostgreSQLDialect")
            .setProperty("hibernate.connection.driver_class", "org.postgresql.Driver")
            .setProperty("hibernate.connection.url", "jdbc:postgresql://localhost:5432/library")
            .setProperty("hibernate.connection.username", "user")
            .setProperty("hibernate.connection.password", "password")
            .setProperty("hibernate.hbm2ddl.auto", "validate") // только валидация!
            .setProperty("hibernate.show_sql", "true")
            .setProperty("hibernate.format_sql", "true")
            .buildSessionFactory();
    }
}
