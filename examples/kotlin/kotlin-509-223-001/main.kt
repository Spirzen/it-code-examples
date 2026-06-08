
import io.mockk.*
import kotlinx.coroutines.test.runTest
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

interface UserRepo {
    suspend fun findName(id: Int): String
}

class UserService(private val repo: UserRepo) {
    suspend fun greet(id: Int) = "Hello, ${repo.findName(id)}!"
}

class UserServiceTest {

    private val repo = mockk<UserRepo>()
    private val service = UserService(repo)

    @Test
    fun greet() = runTest {
        coEvery { repo.findName(1) } returns "Ann"
        assertEquals("Hello, Ann!", service.greet(1))
        coVerify { repo.findName(1) }
    }
}
