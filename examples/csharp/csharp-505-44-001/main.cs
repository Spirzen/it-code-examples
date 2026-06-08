string query = "SELECT Id, Name FROM Users";

using (SqlConnection connection = new SqlConnection(connectionString)) {
    SqlCommand command = new SqlCommand(query, connection);
    connection.Open();

    using (SqlDataReader reader = command.ExecuteReader()) {
        while (reader.Read()) {
            int id = reader.GetInt32(0); // Индекс колонки
            string name = reader.GetString(1);
            Console.WriteLine($"ID: {id}, Имя: {name}");
        }
    }
}
