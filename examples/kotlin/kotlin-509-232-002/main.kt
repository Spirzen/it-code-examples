@WebMvcTest(HelloController::class)
class HelloControllerTest(
    @Autowired val mockMvc: MockMvc
) {
    @MockBean lateinit var service: HelloService

    @Test
    fun returnsHello() {
        whenever(service.greet("Анна")).thenReturn(HelloResponse("Привет, Анна!"))

        mockMvc.get("/api/hello?name=Анна")
            .andExpect { status { isOk() } }
            .andExpect { jsonPath("$.message") { value("Привет, Анна!") } }
    }
}
