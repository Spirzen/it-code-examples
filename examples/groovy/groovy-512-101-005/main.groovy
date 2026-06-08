class UserServiceSpec extends Specification {
    
    UserService userService
    UserRepository userRepository = Mock()
    
    def setup() {
        userService = new UserService(userRepository: userRepository)
    }
    
    def "should return active users only"() {
        given:
        userRepository.findAll() >> [
            new User(status: 'ACTIVE', name: 'Alice'),
            new User(status: 'INACTIVE', name: 'Bob'),
            new User(status: 'ACTIVE', name: 'Charlie')
        ]
        
        when:
        def result = userService.getActiveUsers()
        
        then:
        result.size() == 2
        result*.name == ['Alice', 'Charlie']
    }
    
    def "should throw exception when user not found"() {
        given:
        userRepository.findById(123) >> null
        
        when:
        userService.getUser(123)
        
        then:
        thrown(UserNotFoundException)
    }
}
