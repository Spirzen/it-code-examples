@ExtendWith(MockitoExtension.class)
class UserControllerTest {
    @Mock private UserService userService;
    @InjectMocks private UserController controller;

    @Test
    void save_shouldPersistUser() {
        controller.setName("Тимур");
        String outcome = controller.save();
        
        verify(userService).persist(argThat(u -> "Тимур".equals(u.getName())));
        assertEquals("profile?faces-redirect=true", outcome);
    }
}
