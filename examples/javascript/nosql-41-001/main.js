db.users.updateOne(
  { _id: ObjectId("...") },
  {
    $set: { "profile.lastLogin": new Date() },
    $inc: { "stats.logins": 1 },
    $push: {
      "history": {
        $each: [{ action: "login", ts: new Date() }],
        $position: 0,
        $slice: 10
      }
    }
  },
  { upsert: false }
)
