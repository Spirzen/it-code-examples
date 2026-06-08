from lime.lime_text import LimeTextExplainer
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

import numpy as np

# Подготовка текстовых данных
texts = [
    "отличный продукт быстрая доставка рекомендую",
    "ужасное качество деньги на ветер не покупайте",
    "нормальный товар среднее качество",
    "восхитительно превзошло все ожидания",
    "кошмар полное разочарование",
    "хорошо работает без проблем",
    "отвратительно не соответствует описанию",
    "приемлемо за эти деньги",
    "просто замечательно всем доволен",
    "ужасная поддержка клиентов"
] * 100

labels = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0] * 100  # 1 - позитив, 0 - негатив

# Создание конвейера классификации
vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 2))
classifier = LogisticRegression(max_iter=1000, random_state=42)
pipeline = make_pipeline(vectorizer, classifier)

# Обучение модели
pipeline.fit(texts, labels)

# Создание эксплайнера LIME
class_names = ['негативный', 'позитивный']
explainer = LimeTextExplainer(class_names=class_names)

# Интерпретация прогноза для нового текста
text_to_explain = "отличное качество и очень быстрая доставка"
model_prediction = pipeline.predict([text_to_explain])[0]
model_proba = pipeline.predict_proba([text_to_explain])[0]

print(f"Текст для анализа: '{text_to_explain}'")
print(f"Прогноз модели: {class_names[model_prediction]}")
print(f"Вероятности: негативный={model_proba[0]:.2%}, позитивный={model_proba[1]:.2%}")

# Получение объяснения
explanation = explainer.explain_instance(
    text_to_explain,
    pipeline.predict_proba,
    num_features=10,
    top_labels=1
)

# Вывод важных слов
print("\nВажные слова для позитивного прогноза:")
for word, weight in explanation.as_list(label=1):
    sentiment = "↑" if weight > 0 else "↓"
    print(f"  {word}: {weight:+.4f} {sentiment}")

# Визуализация объяснения
fig = explanation.as_pyplot_figure(label=1)
fig.set_size_inches(10, 6)
plt.title('LIME: Важность слов для прогноза')
plt.tight_layout()
plt.savefig('lime_explanation.png')
plt.close()
