import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.*;

class BoundaryTest {

    @ParameterizedTest
    @CsvSource({
        "0, false",
        "1, true",
        "100, true",
        "-1, false"
    })
    void orderQuantityValidation(int qty, boolean valid) {
        assertEquals(valid, qty > 0 && qty <= 100);
    }
}
