class UserServiceTest : FunSpec({
    test("пользователь с валидным email сохраняется") {
        val user = User(email = "test@example.com")
        val result = userService.save(user)
        result.id shouldNotBe null
        result.email shouldBe "test@example.com"
    }

    context("при недопустимом email") {
        test("выбрасывается исключение") {
            val invalidUser = User(email = "invalid")
            shouldThrow<ValidationException> {
                userService.save(invalidUser)
            }
        }
    }
})
