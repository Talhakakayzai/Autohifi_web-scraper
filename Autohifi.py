import requests
from bs4 import BeautifulSoup
import csv

# Example AutoHifi URL (replace with the real one)
URL = "https://www.autohifi-example.com/products"

# Custom headers to mimic a real browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

def fetch_html(url):
    """Fetch the HTML content of the given URL."""
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.text

def parse_products(html):
    """Parse the HTML and extract product details."""
    soup = BeautifulSoup(html, "html.parser")
    product_elements = soup.find_all("div", class_="product-card")
    
    products = []
    for item in product_elements:
        name = item.find("h2", class_="product-title").get_text(strip=True)
        price = item.find("span", class_="product-price").get_text(strip=True)
        products.append({"name": name, "price": price})
    
    return products

def save_to_csv(products, filename="autohifi_products.csv"):
    """Save product data to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "price"])
        writer.writeheader()
        for product in products:
            writer.writerow(product)

def main():
    print("Scraping AutoHifi website...")
    html = fetch_html(URL)
    products = parse_products(html)
    save_to_csv(products)
    print(f"Scraped {len(products)} products and saved to autohifi_products.csv")

if __name__ == "__main__":
    main()
