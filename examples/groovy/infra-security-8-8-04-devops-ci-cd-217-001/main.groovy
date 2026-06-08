pipeline {
    agent any

    environment {
        NODE_VERSION = '18'
        NPM_REGISTRY = 'https://registry.npmjs.org/'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Node.js') {
            steps {
                sh 'echo "Установка Node.js версии ${NODE_VERSION}"'
                sh 'curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash'
                sh 'source ~/.nvm/nvm.sh && nvm install ${NODE_VERSION} && nvm use ${NODE_VERSION}'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm ci --registry=${NPM_REGISTRY}'
            }
        }

        stage('Run Linter') {
            steps {
                sh 'npm run lint'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'npm test'
            }
        }

        stage('Build') {
            steps {
                sh 'npm run build'
                archiveArtifacts artifacts: 'dist/**/*', fingerprint: true
            }
        }

        stage('Deploy to Staging') {
            when {
                branch 'main'
            }
            steps {
                sh 'scp -r dist/ user@staging-server:/var/www/app/'
                sh 'ssh user@staging-server "sudo systemctl reload nginx"'
            }
        }
    }

    post {
        always {
            echo 'Очистка рабочего пространства'
            deleteDir()
        }
        failure {
            echo 'Сборка завершилась с ошибкой'
            // Здесь может быть отправка уведомления в Slack или Telegram
        }
        success {
            echo 'Сборка успешно завершена'
        }
    }
}
