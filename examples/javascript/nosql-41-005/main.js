// 1. Создать сессию
const session = db.getMongo().startSession();

// 2. Начать транзакцию
session.startTransaction({
  readConcern: { level: "snapshot" },
  writeConcern: { w: "majority", j: true },
  readPreference: "primary"  // обязательно для транзакций
});

try {
  // 3. Выполнять операции в сессии
  db.users.updateOne(
    { _id: ObjectId("..."), balance: { $gte: 100 } },
    { $inc: { balance: -100 } },
    { session: session }
  );

  db.orders.insertOne(
    { userId: ObjectId("..."), amount: 100, ts: new Date() },
    { session: session }
  );

  // 4. Зафиксировать
  session.commitTransaction();
  print("Транзакция успешна");

} catch (error) {
  // 5. Откат при ошибке
  session.abortTransaction();
  throw error;

} finally {
  // 6. Закрыть сессию (важно!)
  session.endSession();
}
