use company_db;

db.createCollection("employees", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["first_name", "last_name", "salary"],
            properties: {
                first_name: { bsonType: "string" },
                last_name: { bsonType: "string" },
                email: {
                    bsonType: "string",
                    pattern: "^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$"
                },
                salary: { bsonType: "number", minimum: 0 },
                department_id: { bsonType: "int", minimum: 1 }
            }
        }
    }
});
