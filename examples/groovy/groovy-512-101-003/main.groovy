// Фильтрация
def activeUsers = users.findAll { it.status == 'ACTIVE' }

// Преобразование
def userEmails = users.collect { it.email }

// Агрегация
def totalBalance = accounts.sum { it.balance ?: 0 }

// Поиск
def admin = users.find { it.role == 'ADMIN' }
def hasPremium = users.any { it.plan == 'PREMIUM' }
def allVerified = users.every { it.emailVerified }

// Группировка
def usersByCountry = users.groupBy { it.country }
