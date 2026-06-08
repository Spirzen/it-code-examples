
import csv
import requests

from bs4 import BeautifulSoup

def scrape_products(url: str) -> list[dict]:
    resp = requests.get(url, headers={"User-Agent": "StudyBot/1.0"}, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")
    rows = []
    for card in soup.select(".product-card"):
        name = card.select_one(".title")
        price = card.select_one(".price")
        if name and price:
            rows.append({
                "name": name.get_text(strip=True),
                "price": price.get_text(strip=True),
            })
    return rows

if __name__ == "__main__":
    data = scrape_products("https://example.com/shop")
    with open("prices.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "price"])
        writer.writeheader()
        writer.writerows(data)
