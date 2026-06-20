// Практикум: https://spirzen.ru/encyclopedia/4-code-dev/4-05-asinhronnost/3

import java.util.concurrent.Executors
import java.util.concurrent.TimeUnit

@Grab('org.codehaus.gpars:gpars:1.2.1')
import groovyx.gpars.GParsPool

def urls = [
    ['https://example.com/page1', 2000L],
    ['https://example.com/page2', 3500L],
    ['https://example.com/page3', 1500L],
    ['https://example.com/page4', 2500L],
    ['https://example.com/page5', 1000L],
]

def download = { String url, long delayMs ->
    Thread.sleep(delayMs)
    println "  Готово: $url"
}

println '=== Groovy — sequential, ExecutorService, GPars ==='

// 1. Последовательно
println '\n1. ПОСЛЕДОВАТЕЛЬНО'
def seqStart = System.currentTimeMillis()
urls.each { url, ms -> download(url, ms) }
def seqElapsed = (System.currentTimeMillis() - seqStart) / 1000.0
println "  Время: ${String.format('%.2f', seqElapsed)} с"

// 2. ExecutorService
println '\n2. EXECUTOR SERVICE'
def poolStart = System.currentTimeMillis()
def pool = Executors.newFixedThreadPool(4)
urls.each { url, ms -> pool.submit { download(url, ms) } }
pool.shutdown()
pool.awaitTermination(1, TimeUnit.MINUTES)
def poolElapsed = (System.currentTimeMillis() - poolStart) / 1000.0
println "  Время: ${String.format('%.2f', poolElapsed)} с"

// 3. GPars
println '\n3. GPARS (.parallel)'
def gparsStart = System.currentTimeMillis()
GParsPool.withPool {
    urls.parallel.each { url, ms -> download(url, ms) }
}
def gparsElapsed = (System.currentTimeMillis() - gparsStart) / 1000.0
println "  Время: ${String.format('%.2f', gparsElapsed)} с"

println '\n--- Итог ---'
println "Последовательно: ${String.format('%.2f', seqElapsed)} с"
println "ExecutorService: ${String.format('%.2f', poolElapsed)} с"
println "GPars:           ${String.format('%.2f', gparsElapsed)} с"
