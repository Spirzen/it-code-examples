pipelineJob('shop-build') {
    description('Сборка shop — ветка main')
    definition {
        cpsScm {
            scm {
                git {
                    remote { url('https://github.com/example/shop.git') }
                    branch('main')
                }
            }
            scriptPath('Jenkinsfile')
        }
    }
    triggers {
        scm('H/15 * * * *')
    }
}
