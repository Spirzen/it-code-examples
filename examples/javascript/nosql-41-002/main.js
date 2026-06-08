// Только name и email, без _id
{ name: 1, email: 1, _id: 0 }

// Все поля, кроме password и tokens
{ password: 0, tokens: 0 }

// Первые 3 элемента массива history
{ history: { $slice: 3 } }

// Последние 2 элемента
{ history: { $slice: -2 } }

// Элементы 5–10 (пропустить 5, взять 5)
{ history: { $slice: [5, 5] } }

// Только первый элемент массива, удовлетворяющий условию
{ "comments": { $elemMatch: { rating: { $gte: 4 } } } }

// Позиционный оператор: вернуть только тот элемент comments, который matched в запросе
db.posts.find(
  { "comments.author": "timur" },
  { "comments.$": 1 }  // → вернёт только первый подходящий комментарий
)
