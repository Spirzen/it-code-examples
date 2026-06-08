// vars/standardPipeline.groovy

def call(Map config = [:]) {
    pipeline {
        agent any

        options {
            timestamps()
            timeout(time: config.timeoutMinutes ?: 30, unit: 'MINUTES')
        }

        stages {
            stage('Checkout') {
                steps {
                    checkout scm
                }
            }

            stage('Test') {
                steps {
                    sh(config.testCommand ?: './gradlew test --no-daemon')
                }
            }

            stage('Deploy') {
                when {
                    expression {
                        config.deploy == true && env.BRANCH_NAME == 'main'
                    }
                }
                steps {
                    sh(config.deployCommand ?: './deploy.sh staging')
                }
            }
        }

        post {
            always {
                junit(config.junitPattern ?: '**/build/test-results/test/*.xml')
            }
            failure {
                notifySlack("Build failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}")
            }
        }
    }
}
