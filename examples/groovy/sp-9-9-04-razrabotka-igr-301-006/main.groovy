pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    sh '''
                        /opt/Unity/Hub/Editor/2022.3.29f1/Editor/Unity \
                          -batchmode \
                          -projectPath "$PWD" \
                          -executeMethod BuildScript.BuildAndroid \
                          -logFile /dev/stdout
                    '''
                }
            }
        }
    }
}
