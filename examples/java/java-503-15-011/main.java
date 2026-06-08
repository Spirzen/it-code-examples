// Вывод для примитивов
var count = 42;                  // int
var price = 199.99;              // double
var isActive = true;             // boolean
var initial = 'A';               // char

// Вывод для ссылочных типов
var name = "Java";               // String
var list = new ArrayList<String>(); // ArrayList<String>
var map = new HashMap<String, Integer>(); // HashMap<String, Integer>

// Вывод для массивов
var numbers = new int[]{1, 2, 3, 4, 5}; // int[]
var strings = new String[]{"a", "b", "c"}; // String[]

// Вывод для сложных типов
var entrySet = map.entrySet();   // Set<Map.Entry<String, Integer>>
var stream = list.stream();      // Stream<String>

// Вывод для результатов методов
var result = calculateSum(10, 20); // тип возвращаемого значения метода
var optional = findUserById(123);  // Optional<User>

// Ограничения использования var
// var x; // ошибка — требуется инициализатор
// var y = null; // ошибка — null не имеет типа
// поле класса: 
//   var field = "value"; // ошибка — var допустим только для локальных переменных

// Плохой пример использования (снижает читаемость)
var data = fetchData(); // что возвращает метод? тип неочевиден

// Хороший пример (тип очевиден из правой части)
var users = new ArrayList<User>();
var config = loadConfigurationFromFile("app.properties");
