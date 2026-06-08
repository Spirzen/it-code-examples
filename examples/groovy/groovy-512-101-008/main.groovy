// config/application.groovy
dataSource {
    pooled = true
    driverClassName = 'org.postgresql.Driver'
    username = System.getenv('DB_USER') ?: 'app_user'
    password = System.getenv('DB_PASSWORD') ?: 'secret'
    url = System.getenv('DB_URL') ?: 'jdbc:postgresql://localhost:5432/app_db'
}

environments {
    development {
        dataSource {
            url = 'jdbc:postgresql://localhost:5432/app_dev'
        }
    }
    production {
        dataSource {
            properties {
                maxActive = 50
                maxIdle = 25
                minIdle = 5
                initialSize = 5
                maxWait = 10000
            }
        }
    }
}
