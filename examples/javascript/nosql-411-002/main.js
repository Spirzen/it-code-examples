db.employees.insertMany([
    {
        first_name: "Maria",
        last_name: "Petrova",
        email: "petrova@example.com",
        hire_date: ISODate("2024-02-10"),
        salary: 82000.00,
        department_id: 2,
        skills: ["Java", "Spring"],
        is_active: true
    },
    {
        first_name: "Alexey",
        last_name: "Sidorov",
        email: "sidorov@example.com",
        hire_date: ISODate("2024-03-01"),
        salary: 65000.00,
        department_id: 1,
        skills: ["C#", ".NET"],
        is_active: false
    }
]);
