
import org.dbunit.database.DatabaseConnection;
import org.dbunit.dataset.IDataSet;
import org.dbunit.dataset.xml.FlatXmlDataSetBuilder;
import org.dbunit.operation.DatabaseOperation;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import javax.sql.DataSource;
import java.sql.Connection;

public class UserServiceTest {

    private DataSource dataSource;
    private Connection connection;

    @BeforeEach
    public void setUp() throws Exception {
        // Инициализация DataSource (например, H2 in-memory)
        dataSource = createDataSource(); 
        connection = dataSource.getConnection();
        
        // Загрузка эталонных данных из XML
        IDataSet dataSet = new FlatXmlDataSetBuilder()
            .setColumnSensing(true)
            .build(new File("src/test/resources/datasets/users.xml"));
            
        DatabaseOperation.CLEAN_INSERT.execute(
            new DatabaseConnection(connection), 
            dataSet
        );
    }

    @Test
    public void testUserCreation() throws Exception {
        // Логика теста: вызов сервиса, который работает с БД
        // ...
        
        // Проверка результата
        // Можно использовать Asserts DBUnit для сравнения текущего состояния с эталоном
    }
}
