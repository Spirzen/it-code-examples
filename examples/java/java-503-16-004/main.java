import java.util.concurrent.ThreadLocalRandom;

// Целое от 0 (включительно) до 101 (исключительно) → 0..100
int x = ThreadLocalRandom.current().nextInt(0, 101);

// Кубик: 1..6
int dice = ThreadLocalRandom.current().nextInt(1, 7);

// Случайный индекс массива или списка
String[] cities = {"Москва", "Казань", "Новосибирск"};
int index = ThreadLocalRandom.current().nextInt(cities.length);
String pick = cities[index];

// Вещественное от 0.0 до 1.0 (как Math.random(), но через тот же API)
double fraction = ThreadLocalRandom.current().nextDouble();
