class AdaptiveWindowClassifier:
    def __init__(self, base_classifier, window_size=1000, drift_threshold=0.1):
        self.base_classifier = base_classifier
        self.window_size = window_size
        self.drift_threshold = drift_threshold
        self.X_window = []
        self.y_window = []
        self.accuracy_history = []
        self.drift_points = []
    
    def partial_fit(self, X, y):
        # Добавление новых данных в окно
        self.X_window.extend(X)
        self.y_window.extend(y)
        
        # Ограничение размера окна
        if len(self.X_window) > self.window_size:
            removed = len(self.X_window) - self.window_size
            self.X_window = self.X_window[-self.window_size:]
            self.y_window = self.y_window[-self.window_size:]
        
        # Обучение на текущем окне
        self.base_classifier.partial_fit(
            np.array(self.X_window), 
            np.array(self.y_window),
            classes=np.unique(y)
        )
    
    def detect_drift(self, X_new, y_new):
        # Оценка качества на новом пакете
        accuracy_new = self.base_classifier.score(X_new, y_new)
        self.accuracy_history.append(accuracy_new)
        
        # Проверка дрейфа при достаточном объёме истории
        if len(self.accuracy_history) > 5:
            recent_mean = np.mean(self.accuracy_history[-5:])
            historical_mean = np.mean(self.accuracy_history[:-5]) if len(self.accuracy_history) > 10 else recent_mean
            
            if historical_mean - recent_mean > self.drift_threshold:
                self.drift_points.append(len(self.accuracy_history))
                print(f"Обнаружен концепт-дрейф на шаге {len(self.accuracy_history)}: "
                      f"точность упала с {historical_mean:.4f} до {recent_mean:.4f}")
                return True
        return False

# Имитация данных с изменяющимся распределением
np.random.seed(42)
X_stream = []
y_stream = []

# Первый сегмент данных
X1, y1 = make_classification(n_samples=2000, n_features=20, n_informative=15, random_state=42)
X_stream.append(X1)
y_stream.append(y1)

# Второй сегмент с изменёнными параметрами
X2, y2 = make_classification(n_samples=2000, n_features=20, n_informative=15, 
                            flip_y=0.2, random_state=100)  # повышенный шум
X_stream.append(X2)
y_stream.append(y2)

# Третий сегмент с новыми информативными признаками
X3, y3 = make_classification(n_samples=2000, n_features=20, n_informative=10, 
                            n_redundant=10, random_state=200)
X_stream.append(X3)
y_stream.append(y3)

X_full = np.vstack(X_stream)
y_full = np.hstack(y_stream)

# Обучение с обнаружением дрейфа
classifier = SGDClassifier(loss='log_loss', random_state=42)
adaptive_clf = AdaptiveWindowClassifier(classifier, window_size=500, drift_threshold=0.08)

batch_size = 100
for i in range(0, len(X_full), batch_size):
    X_batch = X_full[i:i+batch_size]
    y_batch = y_full[i:i+batch_size]
    
    adaptive_clf.partial_fit(X_batch, y_batch)
    
    # Проверка дрейфа каждые 5 пакетов
    if i % (5 * batch_size) == 0 and i > 0:
        adaptive_clf.detect_drift(X_full[max(0, i-500):i], y_full[max(0, i-500):i])
