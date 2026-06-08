pipeline {
    agent any
    stages {
        stage("Test") {
            steps {
                sh "./gradlew test --no-daemon"
            }
        }
        stage("Approve") {
            steps {
                input message: "Выкатить каталог в production", ok: "Deploy"
            }
        }
    }
    post {
        always { junit "**/build/test-results/test/*.xml" }
    }
}
