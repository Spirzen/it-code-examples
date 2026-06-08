{
  $facet: {
    byStatus: [
      { $group: { _id: "$status", count: { $sum: 1 } } }
    ],
    topUsers: [
      { $group: { _id: "$user", total: { $sum: "$amount" } } },
      { $sort: { total: -1 } },
      { $limit: 5 }
    ],
    stats: [
      { $group: {
          _id: null,
          avg: { $avg: "$amount" },
          max: { $max: "$amount" },
          min: { $min: "$amount" }
      } }
    ]
  }
}
