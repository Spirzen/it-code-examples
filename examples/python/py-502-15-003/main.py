# Избыточная абстракция
class DataProcessor:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def process(self, Данные):
        return self.strategy.execute(Данные)

class DoubleStrategy:
    def execute(self, Данные):
        return [x * 2 for x in Данные]

processor = DataProcessor(DoubleStrategy())
result = processor.process([1, 2, 3])

# Простая функция решает ту же задачу
def double_values(Данные):
    return [x * 2 for x in Данные]

result = double_values([1, 2, 3])
