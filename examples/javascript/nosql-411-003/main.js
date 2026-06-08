db.employees.aggregate([
  {
    $lookup: {
      from: "departments",
      localField: "department_id",
      foreignField: "_id",
      as: "department"
    }
  },
  { $unwind: { path: "$department", preserveNullAndEmptyArrays: true } },
  {
    $project: {
      first_name: 1,
      last_name: 1,
      deptName: "$department.name"
    }
  }
]);
