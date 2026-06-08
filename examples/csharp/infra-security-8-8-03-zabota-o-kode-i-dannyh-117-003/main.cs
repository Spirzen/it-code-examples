// Пример восстановления через .NET приложение
using System.Data.SqlClient;
using System.IO;

string connectionString = "Server=localhost;Database=master;User Id=sa;";
string dumpFile = @"/backup/db_backup.sql";
string command = File.ReadAllText(dumpFile);

using (var connection = new SqlConnection(connectionString))
{
    connection.Open();
    var cmd = new SqlCommand(command, connection);
    cmd.ExecuteNonQuery();
}
