// Создать
db.coll.createIndex({ a: 1 }, { name: "idx_a", unique: true })

// Посмотреть все
db.coll.getIndexes()

// Удалить по имени
db.coll.dropIndex("idx_a")

// Удалить по спецификации
db.coll.dropIndex({ a: 1 })

// Удалить все (кроме _id)
db.coll.dropIndexes()

// Статистика по использованию (требует serverStatus или профилирование)
db.coll.aggregate([{ $indexStats: {} }])
