<?php
// Демонстрация переменных
$siteTitle = "Демонстрация возможностей PHP";
$version = "8.2";
$currentYear = date("Y");
$features = [
    "Переменные и типы данных",
    "Операторы и выражения", 
    "Циклы и условия",
    "Функции",
    "Классы и объекты",
    "Работа с массивами"
];

// Демонстрация операторов
$calculationResult = (10 + 5) * 2;
$comparison = 15 > 10;
$logical = true && false;

// Демонстрация функций
function calculateDiscount($price, $discount = 0.1) {
    return $price * (1 - $discount);
}

function formatCurrency($amount) {
    return number_format($amount, 2, ',', ' ') . " ₽";
}

// Демонстрация классов и объектов
class Product {
    private string $name;
    private float $price;
    private int $stock;
    
    public function __construct(string $name, float $price, int $stock = 0) {
        $this->name = $name;
        $this->price = $price;
        $this->stock = $stock;
    }
    
    public function getName(): string {
        return $this->name;
    }
    
    public function getPrice(): float {
        return $this->price;
    }
    
    public function getStock(): int {
        return $this->stock;
    }
    
    public function isAvailable(): bool {
        return $this->stock > 0;
    }
    
    public function getDiscountedPrice(float $discount = 0.1): float {
        return $this->price * (1 - $discount);
    }
}

class ProductCatalog {
    private array $products = [];
    
    public function addProduct(Product $product): void {
        $this->products[] = $product;
    }
    
    public function getProducts(): array {
        return $this->products;
    }
    
    public function getProductCount(): int {
        return count($this->products);
    }
}

// Создание каталога продуктов
$catalog = new ProductCatalog();
$catalog->addProduct(new Product("Ноутбук", 59999.00, 5));
$catalog->addProduct(new Product("Смартфон", 29999.00, 10));
$catalog->addProduct(new Product("Наушники", 5999.00, 15));
$catalog->addProduct(new Product("Монитор", 19999.00, 8));

// Демонстрация работы с массивами
$prices = array_map(fn($product) => $product->getPrice(), $catalog->getProducts());
$averagePrice = array_sum($prices) / count($prices);
$minPrice = min($prices);
$maxPrice = max($prices);

// Демонстрация циклов
$productsHtml = "";
foreach ($catalog->getProducts() as $product) {
    $productsHtml .= "
        <div class='product-card'>
            <h3>{$product->getName()}</h3>
            <p class='price'>Цена: " . formatCurrency($product->getPrice()) . "</p>
            <p class='stock'>Наличие: " . ($product->isAvailable() ? "В наличии ({$product->getStock()})" : "Нет в наличии") . "</p>
            <p class='discount'>Со скидкой: " . formatCurrency($product->getDiscountedPrice()) . "</p>
        </div>";
}

// Демонстрация условий
$statusMessage = $catalog->getProductCount() > 0 
    ? "Каталог содержит {$catalog->getProductCount()} товаров"
    : "Каталог пуст";
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $siteTitle; ?> - PHP <?php echo $version; ?></title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 60px 40px;
            text-align: center;
        }
        
        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
        }
        
        .subtitle {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .content {
            padding: 40px;
        }
        
        section {
            margin-bottom: 40px;
        }
        
        h2 {
            color: #667eea;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }
        
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .feature-item {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }
        
        .demo-box {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin-top: 20px;
        }
        
        .demo-box h3 {
            color: #764ba2;
            margin-bottom: 15px;
        }
        
        .demo-box p {
            margin: 10px 0;
        }
        
        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .product-card {
            background: #f8f9fa;
            padding: 25px;
            border-radius: 8px;
            border: 2px solid #e9ecef;
        }
        
        .product-card h3 {
            color: #333;
            margin-bottom: 15px;
        }
        
        .price {
            font-weight: bold;
            color: #28a745;
            font-size: 1.2em;
        }
        
        .stock {
            color: #667eea;
            margin: 10px 0;
        }
        
        .discount {
            color: #dc3545;
            font-weight: bold;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .stat-item {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }
        
        .stat-value {
            font-size: 2em;
            font-weight: bold;
            margin: 10px 0;
        }
        
        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1><?php echo $siteTitle; ?></h1>
            <p class="subtitle">Интерактивная демонстрация основных возможностей языка программирования PHP <?php echo $version; ?></p>
        </header>
        
        <div class="content">
            <section>
                <h2>Основные возможности</h2>
                <div class="feature-grid">
                    <?php foreach ($features as $feature): ?>
                        <div class="feature-item">
                            <h3><?php echo $feature; ?></h3>
                        </div>
                    <?php endforeach; ?>
                </div>
            </section>
            
            <section>
                <h2>Демонстрация синтаксиса</h2>
                <div class="demo-box">
                    <h3>Переменные и операторы</h3>
                    <p>Результат вычисления (10 + 5) × 2 = <strong><?php echo $calculationResult; ?></strong></p>
                    <p>Сравнение 15 > 10: <strong><?php echo $comparison ? "true" : "false"; ?></strong></p>
                    <p>Логическое выражение true && false: <strong><?php echo $logical ? "true" : "false"; ?></strong></p>
                </div>
                
                <div class="demo-box">
                    <h3>Функции</h3>
                    <p>Пример функции скидки: исходная цена 10000 ₽, скидка 10%</p>
                    <p>Итоговая цена: <strong><?php echo formatCurrency(calculateDiscount(10000)); ?></strong></p>
                </div>
            </section>
            
            <section>
                <h2>Каталог продуктов</h2>
                <p><?php echo $statusMessage; ?></p>
                <div class="products-grid">
                    <?php echo $productsHtml; ?>
                </div>
                
                <div class="stats-grid">
                    <div class="stat-item">
                        <div>Средняя цена</div>
                        <div class="stat-value"><?php echo formatCurrency($averagePrice); ?></div>
                    </div>
                    <div class="stat-item">
                        <div>Минимальная цена</div>
                        <div class="stat-value"><?php echo formatCurrency($minPrice); ?></div>
                    </div>
                    <div class="stat-item">
                        <div>Максимальная цена</div>
                        <div class="stat-value"><?php echo formatCurrency($maxPrice); ?></div>
                    </div>
                </div>
            </section>
            
            <section>
                <h2>Статистика</h2>
                <div class="demo-box">
                    <p>Всего товаров в каталоге: <strong><?php echo $catalog->getProductCount(); ?></strong></p>
                    <p>Текущий год: <strong><?php echo $currentYear; ?></strong></p>
                    <p>Версия демонстрации: <strong><?php echo $version; ?></strong></p>
                </div>
            </section>
        </div>
        
        <footer>
            <p>© <?php echo $currentYear; ?> Демонстрация возможностей PHP. Создано с использованием современных возможностей языка.</p>
        </footer>
    </div>
</body>
</html>
