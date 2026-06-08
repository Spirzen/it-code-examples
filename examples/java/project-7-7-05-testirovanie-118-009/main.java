
import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(
    features = "src/test/java/features",
    glue = {"io.karatelabs"},
    monochrome = true,
    plugin = {"html:target/karate-reports", "json:target/karate-results.json"}
)
public class KarateTest {
    // Класс служит точкой входа для запуска всех сценариев
}
