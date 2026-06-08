   import logging
   from typing import Optional
   import json

   logger = logging.getLogger(__name__)

   def get_article(slug: str, db) -> Optional[dict]:
       cache_key = f"article:{slug}"

       # Получаем из кэша
       cached = cache.get(cache_key)
       if cached is not None:
           return cached  # pymemcache уже десериализовал через JSON

       # Промах
       try:
           row = db.execute(
               "SELECT id, title, body, author_id FROM articles WHERE slug = %s",
               (slug,)
           ).fetchone()

           if not row:
               return None

           article = {
               "id": row[0],
               "title": row[1],
               "body": row[2],
               "author_id": row[3]
           }

           # Сохраняем с TTL = 300 сек
           cache.set(cache_key, article, expire=300)
           return article

       except Exception as e:
           logger.exception("DB error for article %s", slug)
           return None  # graceful degradation
