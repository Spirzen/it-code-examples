// Неправильно: структура с множеством несвязанных обязанностей
struct UserProcessor {
    users: Vec<User>,
    database: DatabaseConnection,
    email_client: SmtpClient,
    logger: Logger,
}

// Правильно: разделение ответственности
struct UserRepository {
    connection: DatabaseConnection,
}

struct EmailService {
    client: SmtpClient,
}

struct UserProcessor {
    repository: UserRepository,
    email_service: EmailService,
}
