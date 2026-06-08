   {
     $lookup: {
       from: "orders",
       let: { userId: "$_id", status: "$premium" },
       pipeline: [
         { $match: {
             $expr: {
               $and: [
                 { $eq: ["$userId", "$$userId"] },
                 { $gte: ["$amount", { $cond: ["$$status", 1000, 500] }] }
               ]
             }
           }
         },
         { $project: { _id: 0, date: 1, amount: 1 } }
       ],
       as: "bigOrders"
     }
   }
