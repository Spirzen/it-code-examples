val collection = db.getCollection<Document>("users")

// Вставка
collection.insertOne(
    documentOf(
        "name" to "Олег",
        "email" to "oleg@example.com",
        "tags" to listOf("dev", "kotlin")
    )
)

// Поиск (типобезопасно через кодеки)
val codecRegistry = fromRegistries(
    MongoClientSettings.getDefaultCodecRegistry(),
    fromProviders(PojoCodecProvider.builder().automatic(true).build())
)

val userCollection = db.getCollection<User>("users").withCodecRegistry(codecRegistry)
val user = userCollection.find(eq("email", "oleg@example.com")).first()
