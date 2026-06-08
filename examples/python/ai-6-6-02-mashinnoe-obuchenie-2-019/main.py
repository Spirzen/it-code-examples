from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_20newsgroups

# Классификация текстов
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics']
newsgroups = fetch_20newsgroups(subset='all', categories=categories, remove=('headers', 'footers', 'quotes'))

# Векторизация текста
vectorizer = CountVectorizer(stop_words='english', max_features=5000)
X = vectorizer.fit_transform(newsgroups.data)
y = newsgroups.target

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели
clf = MultinomialNB(alpha=0.1)
clf.fit(X_train, y_train)

# Прогнозирование
predictions = clf.predict(X_test)

# Анализ важности слов для классов
feature_names = vectorizer.get_feature_names_out()
for i, class_label in enumerate(clf.classes_):
    top_indices = clf.feature_log_prob_[i].argsort()[-10:][::-1]
    top_words = [feature_names[idx] for idx in top_indices]
