/**
 * Практикум: https://spirzen.ru/encyclopedia/4-code-dev/4-05-asinhronnost/3
 *
 * Зависимость: org.jetbrains.kotlinx:kotlinx-coroutines-core
 */
import kotlinx.coroutines.async
import kotlinx.coroutines.awaitAll
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking

suspend fun download(url: String, delayMs: Long): String {
    delay(delayMs)
    return "Данные с $url"
}

suspend fun loadAllSequential(urls: List<Pair<String, Long>>) {
    println("\n1. ПОСЛЕДОВАТЕЛЬНО")
    val start = System.currentTimeMillis()
    urls.forEach { (url, ms) ->
        download(url, ms)
        println("  Готово: $url")
    }
    val elapsed = System.currentTimeMillis() - start
    println("  Время: ${elapsed / 1000.0} с")
}

suspend fun loadAllParallel(urls: List<Pair<String, Long>>) = coroutineScope {
    println("\n2. ПАРАЛЛЕЛЬНО (async + awaitAll)")
    val start = System.currentTimeMillis()
    urls
        .map { (url, ms) ->
            async {
                val data = download(url, ms)
                println("  Готово: $url")
                data
            }
        }
        .awaitAll()
    val elapsed = System.currentTimeMillis() - start
    println("  Время: ${elapsed / 1000.0} с")
}

fun main() = runBlocking {
    val urls = listOf(
        "https://example.com/page1" to 2000L,
        "https://example.com/page2" to 3500L,
        "https://example.com/page3" to 1500L,
        "https://example.com/page4" to 2500L,
        "https://example.com/page5" to 1000L,
    )

    println("=== Kotlin — sequential vs async/awaitAll ===")
    loadAllSequential(urls)
    loadAllParallel(urls)
}
