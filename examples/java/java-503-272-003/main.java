
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.security.test.context.support.WithMockUser;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfigureMockMvc
class ApiControllerTest {

    @Autowired MockMvc mvc;

    @Test
    void publicOk() throws Exception {
        mvc.perform(get("/api/public")).andExpect(status().isOk());
    }

    @Test
    void privateUnauthorized() throws Exception {
        mvc.perform(get("/api/private")).andExpect(status().isUnauthorized());
    }

    @Test
    @WithMockUser(username = "demo")
    void privateWithUser() throws Exception {
        mvc.perform(get("/api/private")).andExpect(status().isOk());
    }
}
