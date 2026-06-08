// 1. Добавить новое поле (без downtime)
db.users.updateMany(
  { address: { $exists: true } },
  [{ $set: { addressId: { $toString: "$_id" } } }]
)

// 2. Создать коллекцию addresses
db.users.aggregate([
  { $match: { address: { $exists: true } } },
  { $project: {
      _id: "$addressId",
      userId: "$_id",
      street: "$address.street",
      city: "$address.city"
  } },
  { $out: "addresses" }
])

// 3. Удалить address из users (постепенно, пачками — updateMany не поддерживает limit)
while (db.users.countDocuments({ address: { $exists: true } }) > 0) {
  const batch = db.users.find({ address: { $exists: true } }).limit(1000).toArray();
  if (batch.length === 0) break;
  db.users.bulkWrite(
    batch.map((doc) => ({
      updateOne: { filter: { _id: doc._id }, update: { $unset: { address: "" } } }
    }))
  );
}
