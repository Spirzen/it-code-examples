package utils;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static org.junit.jupiter.api.Assertions.*;

class StringUtilsTest {

    @Test
    @DisplayName("Пустая строка распознаётся как blank")
    void blankStringIsBlank() {
        assertTrue(StringUtils.isBlank(""));
        assertTrue(StringUtils.isBlank("   "));
    }

    @Test
    @DisplayName("Непустая строка не blank")
    void nonBlankString() {
        assertFalse(StringUtils.isBlank("qa"));
    }
}
