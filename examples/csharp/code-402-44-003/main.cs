// Классическая проверка
if (order == null) {
    return NotFound();
}

// Оператор нулевого слияния
string description = product.Description ?? "Описание отсутствует";

// Оператор условного доступа
int? orderCount = shoppingCart?.Items?.Count;

// Pattern matching (C# 7.0+)
if (response is not null) {
    ProcessResponse(response);
}

// Nullable reference types (C# 8.0+)
#nullable enable
string? nullableString = null; // Разрешено
string nonNullableString = "значение"; // Не может быть null
#nullable disable
