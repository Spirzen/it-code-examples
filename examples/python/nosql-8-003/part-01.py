   from pymemcache.client.hash import HashClient
   from pymemcache.serde import json_serializer, json_deserializer

   # Серверы кластера
   servers = [
       ('10.0.1.10', 11211),
       ('10.0.1.11', 11211),
       ('10.0.1.12', 11211),
   ]

   # Клиент с сериализацией JSON и retry
   cache = HashClient(
       servers,
       use_pooling=True,
       pool_size=4,
       pool_maxsize=16,
       serializer=json_serializer,
       deserializer=json_deserializer,
       connect_timeout=1.0,
       timeout=0.5,
       no_delay=True,  # уменьшает задержки TCP
       ignore_exc=True  # при ошибке кэша — не падаем, возвращаем None
   )
