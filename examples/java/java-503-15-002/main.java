// float — 4 байта, одинарная точность
float piApprox = 3.14159265f;    // приближение числа Пи
float temperatureCelsius = 36.6f; // температура тела
float[] vertexCoordinates = {1.0f, 2.5f, -3.7f}; // координаты вершины в 3D

// double — 8 байт, двойная точность (стандартный выбор)
double pi = 3.141592653589793;   // более точное значение Пи
double balance = 12345.67;       // баланс счёт (для отображения, не для расчётов!)
double speedOfLight = 299_792_458.0; // скорость света в м/с
double[] sensorData = {1.23456789, 2.34567890, 3.45678901}; // данные датчиков

// Особые значения в соответствии со стандартом IEEE 754
double positiveInfinity = Double.POSITIVE_INFINITY;
double negativeInfinity = Double.NEGATIVE_INFINITY;
double notANumber = Double.NaN;

// Проверка особых значений
boolean isFinite = Double.isFinite(123.45); // true
boolean isNaN = Double.isNaN(notANumber);   // true
