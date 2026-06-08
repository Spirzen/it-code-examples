// Допустимо для циклов
for (int i = 0; i < items.size(); i++) { }

// Допустимо для координат и математических переменных
double x = point.getX();
double y = point.getY();

// Хорошо
List<User> activeUsers = userRepository.findActive();
int retryCount = 0;

// Плохо
List<User> au = userRepository.findActive(); // непонятная аббревиатура
int rc = 0; // неочевидное сокращение
