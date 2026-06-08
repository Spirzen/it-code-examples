from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

import pandas as pd

# Создание набора транзакций
transactions = [
    ['хлеб', 'молоко', 'яйца'],
    ['хлеб', 'молоко', 'сыр'],
    ['хлеб', 'яйца', 'сыр'],
    ['молоко', 'яйца', 'сыр'],
    ['хлеб', 'молоко', 'яйца', 'сыр'],
    ['хлеб', 'молоко'],
    ['молоко', 'сыр'],
    ['хлеб', 'сыр'],
    ['хлеб', 'молоко', 'яйца', 'масло'],
    ['хлеб', 'яйца', 'масло']
]

# Кодирование транзакций в двоичную матрицу
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Поиск частых наборов с минимальной поддержкой 0.3
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)

# Генерация правил с минимальной достоверностью 0.7
rules = association_rules(
    frequent_itemsets, 
    metric="confidence", 
    min_threshold=0.7
)

# Сортировка правил по подъёму
rules_sorted = rules.sort_values('lift', ascending=False)

# Вывод значимых правил
print("Частые наборы элементов:")
print(frequent_itemsets)
print("\nАссоциативные правила:")
print(rules_sorted[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
