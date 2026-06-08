# Dev — локально или общий стенд команды
APP_ENV=development
DATABASE_URL=postgres://dev-db/app
LOG_LEVEL=debug

# Stage — копия prod по топологии, тестовые/анонимизированные данные
APP_ENV=staging
DATABASE_URL=postgres://stage-db/app
LOG_LEVEL=info

# Prod — только после приёмки и согласованного релиза
APP_ENV=production
DATABASE_URL=postgres://prod-db/app
LOG_LEVEL=warn
