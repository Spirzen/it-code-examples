
import requests

from bs4 import BeautifulSoup

import csv

def scrape_prices(url):
    headers = {'User-Agent': 'Data Scraper 1.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'
    except requests.RequestException as e:
        print(f"Не удалось загрузить страницу: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    products = []

    for item in soup.find_all('div', class_='product-item'):
        title_elem = item.find('h3', class_='title')
        price_elem = item.find('span', class_='price')
        link_elem = item.find('a', href=True)

        if not all([title_elem, price_elem, link_elem]):
            continue  # Пропускаем повреждённые карточки

        title = title_elem.get_text(strip=True)
        price_text = price_elem.get_text(strip=True).replace('₽', '').replace(' ', '')
        
        try:
            price = float(price_text)
        except ValueError:
            price = None

        link = link_elem['href']
        if not link.startswith('http'):
            link = 'https://shop.example.com' + link  # Формируем полный URL

        products.append({
            'title': title,
            'price': price,
            'url': link
        })

    return products

# Запуск
data = scrape_prices('https://shop.example.com/category/laptops')

# Сохранение в CSV
with open('prices.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'price', 'url'])
    writer.writeheader()
    writer.writerows(data)
