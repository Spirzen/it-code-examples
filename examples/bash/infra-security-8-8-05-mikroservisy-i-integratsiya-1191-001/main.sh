# Роли процесса (и брокер, и контроллер в одном узле)
process.roles=broker,controller
node.id=1
controller.quorum.voters=1@localhost:9093

# Слушатели для разных протоколов
listeners=CONTROLLER://localhost:9093,PLAINTEXT://localhost:9092

# Объявляем, какой listener используется для контроллера
controller.listener.names=CONTROLLER

# Маппинг протоколов безопасности (CONTROLLER использует PLAINTEXT)
listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT

# Папка для данных (создайте эту папку или укажите существующую)
log.dirs=C:/kafka/Данные

# Базовые настройки (можно менять по желанию)
num.partitions=1
default.replication.factor=1
offsets.topic.replication.factor=1
transaction.state.log.replication.factor=1
transaction.state.log.min.isr=1
log.retention.hours=168
log.segment.bytes=1073741824
log.retention.check.interval.ms=300000

# Адрес для клиентов (важно!)
advertised.listeners=PLAINTEXT://localhost:9092
