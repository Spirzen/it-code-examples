{
  $setWindowFields: {
    partitionBy: "$department",
    sortBy: { salary: -1 },
    output: {
      rank: { $rank: {} },
      movingAvg: {
        $derivative: { // или $avg, $sum, $min, $max, $stdDevPop, $stdDevSamp
          input: "$salary",
          unit: "month"
        },
        window: { documents: [-2, 0] }  // текущий + 2 предыдущих
      },
      cumulativeCount: {
        $documentNumber: {},
        window: { documents: ["unbounded", "current"] }
      }
    }
  }
}
