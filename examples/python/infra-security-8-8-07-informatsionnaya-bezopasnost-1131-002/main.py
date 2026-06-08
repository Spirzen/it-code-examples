
import zapv2
import time

zap = zapv2.ZAPv2(apikey='myapikey', proxies={'http': 'http://localhost:8080'})

target = 'http://test-application.local'
print(f'Запуск сканирования цели {target}')

# Spidering для обнаружения всех эндпоинтов
print('Запуск спайдера')
zap.spider.scan(target)
time.sleep(2)

while int(zap.spider.status()) < 100:
    print(f'Спайдер прогресс: {zap.spider.status()}%')
    time.sleep(2)

print('Спайдер завершен')

# Активное сканирование
print('Запуск активного сканирования')
zap.ascan.scan(target)
while int(zap.ascan.status()) < 100:
    print(f'Активное сканирование прогресс: {zap.ascan.status()}%')
    time.sleep(5)

print('Сканирование завершено')
print('Уязвимости найдены:')
alerts = zap.core.alerts(baseurl=target)
for alert in alerts:
    print(f"{alert['risk']} - {alert['name']} на {alert['url']}")
