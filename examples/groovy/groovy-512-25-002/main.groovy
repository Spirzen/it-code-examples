job('hello-groovy-nightly') {
    description('Ночной прогон тестов hello-groovy')
    scm {
        git {
            remote { url('https://github.com/example/hello-groovy.git') }
            branch('main')
        }
    }
    triggers {
        cron('H 2 * * *')
    }
    steps {
        shell('./gradlew test --no-daemon')
    }
    publishers {
        junit('**/build/test-results/test/*.xml')
    }
}
