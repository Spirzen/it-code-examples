import com.example.ci.DeployHelper

def call(Map config) {
    pipeline {
        agent any
        stages {
            stage('Deploy') {
                steps {
                    script {
                        def helper = new DeployHelper(this)
                        helper.deploy(config.env ?: 'staging')
                    }
                }
            }
        }
    }
}
