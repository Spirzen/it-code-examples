db.employees.aggregate([
    {
        $lookup: {
            from: "departments",
            localField: "department_id",
            foreignField: "_id",
            as: "dept"
        }
    },
    {
        $unwind: "$dept"
    },
    {
        $group: {
            _id: "$dept.name",
            emp_count: { $sum: 1 },
            total_salary: { $sum: "$salary" },
            avg_salary: { $avg: "$salary" }
        }
    },
    {
        $project: {
            _id: 0,
            department_name: "$_id",
            employee_count: "$emp_count",
            total_fund: "$total_salary",
            average_salary: "$avg_salary"
        }
    }
]).forEach(function(doc) {
    print("Отдел: " + doc.department_name + ", Количество сотрудников: " + doc.employee_count + ", Общий фонд: " + doc.total_fund);
});
