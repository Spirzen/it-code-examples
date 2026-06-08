import io.mockk.coEvery
import io.mockk.coVerifyOrder
import io.mockk.mockk
import kotlinx.coroutines.test.runTest
import org.junit.jupiter.api.Test

interface AuditRepo {
    suspend fun start()
    suspend fun save()
    suspend fun finish()
}

class AuditService(private val repo: AuditRepo) {
    suspend fun execute() {
        repo.start()
        repo.save()
        repo.finish()
    }
}

class AuditServiceTest {
    private val repo = mockk<AuditRepo>()
    private val service = AuditService(repo)

    @Test
    fun executeCallsInOrder() = runTest {
        coEvery { repo.start() } returns Unit
        coEvery { repo.save() } returns Unit
        coEvery { repo.finish() } returns Unit

        service.execute()

        coVerifyOrder {
            repo.start()
            repo.save()
            repo.finish()
        }
    }
}
