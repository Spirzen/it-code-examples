folder('backend') {
    description('Сервисы backend-команды')
}

pipelineJob('backend/api-gateway') {
    definition {
        cpsScm {
            scm {
                git { remote { url('https://github.com/example/gateway.git') } }
            }
            scriptPath('Jenkinsfile')
        }
    }
}

listView('backend/all') {
    description('Все jobs backend')
    jobs { regex('backend/.*') }
    columns {
        status()
        weather()
        name()
        lastSuccess()
        lastFailure()
    }
}
