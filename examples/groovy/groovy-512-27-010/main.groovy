package apitester

import apitester.jmeter.JMeterHttpExecutor
import apitester.model.HttpRequestConfig

class SmokeTest {

    static void main(String[] args) {
        def executor = new JMeterHttpExecutor()
        def config = new HttpRequestConfig(
            url: args ? args[0] : 'https://httpbin.org/get',
            method: 'GET'
        )

        def result = executor.execute(config)
        println "status=${result.statusCode} time=${result.responseTimeMs}ms success=${result.success}"

        if (result.errorMessage) {
            println "error=${result.errorMessage}"
        }

        if (!result.success || result.statusCode != 200) {
            System.exit(1)
        }
    }
}
