q = {'NAME': 'JOHN', 'AGE': 43}

q.get('NAME')              # 'JOHN'
q.get('CITY')              # None — ключа нет, ошибки нет

list(q.keys())             # ['NAME', 'AGE']
list(q.values())           # ['JOHN', 43]

q.update({'STATE': 'CA'})  # {'NAME': 'JOHN', 'AGE': 43, 'STATE': 'CA'}

list(q.items())
# [('NAME', 'JOHN'), ('AGE', 43), ('STATE', 'CA')]

q.setdefault('PIN', 58796) # добавляет PIN, возвращает 58796
# {'NAME': 'JOHN', 'AGE': 43, 'STATE': 'CA', 'PIN': 58796}

q.pop('STATE')             # 'CA' — удалённый ключ; PIN остаётся последним
q.popitem()                # ('PIN', 58796) — снимается последняя вставленная пара

q.clear()                  # {}
