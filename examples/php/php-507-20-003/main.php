// 1. ПОДГОТОВКА - создаем $stmt с SQL-шаблоном
$stmt = $this->db->prepare("INSERT INTO users (name, age) VALUES (?, ?)");

// 2. ПРИВЯЗКА - заменяем ? на переменные
$name = "John";
$age = 25;
$stmt->bind_param("si", $name, $age);  // "s" для name, "i" для age

// 3. ВЫПОЛНЕНИЕ - отправляем запрос в БД
$stmt->execute();

// 4. ОПЦИОНАЛЬНО - для SELECT запросов получаем данные
$result = $stmt->get_result();
$user = $result->fetch_assoc();

// 5. ЗАКРЫТИЕ - освобождаем ресурсы
$stmt->close();
