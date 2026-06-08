db.createView("employee_salary_view", "employees", [
    {
        $lookup: {
            from: "departments",
            localField: "department_id",
            foreignField: "_id",
            as: "dept_info"
        }
    },
    {
        $unwind: "$dept_info"
    },
    {
        $project: {
            first_name: 1,
            last_name: 1,
            department_name: "$dept_info.name",
            salary: 1
        }
    }
]);
