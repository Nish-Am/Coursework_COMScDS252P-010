import requests
from bs4 import BeautifulSoup
import csv
import time
import random

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

headers = {
    "User-Agent": "Mozilla/5.0"
}

books_data = []

def get_page(url, retries=3):
    '''  Fetch page with retry logic   '''
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f'Attempt {attempt + 1} failed for {url}: {e}')
            if attempt < retries - 1:
                time.sleep(2)
            else:
                print('Skipping page after 3 failed attempts.')
                return None


def extract_star_rating(star_class):
    ''' Convert star rating text to number '''

    rating_dict = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    for key in rating_dict:
        if key in star_class:
            return rating_dict[key]
    return None


# Scrape 5 pages (100 books minimum)
for page in range(1, 6):
    url = BASE_URL.format(page)
    print(f'Scraping Page {page}...')

    response = get_page(url)

    if response is None:
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        try:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.strip()
            availability = book.find("p", class_="instock availability").text.strip()
            star_class = book.find("p")["class"]
            rating = extract_star_rating(" ".join(star_class))

            # Get book detail page to extract category
            detail_url = book.h3.a["href"]
            detail_url = "http://books.toscrape.com/catalogue/" + detail_url

            detail_response = get_page(detail_url)
            if detail_response:
                detail_soup = BeautifulSoup(detail_response.text, "html.parser")
                category = detail_soup.find("ul", class_="breadcrumb").find_all("a")[2].text
            else:
                category = "N/A"

            books_data.append([
                title,
                price,
                rating,
                category,
                availability
            ])

        except Exception as e:
            print(f"Error processing book: {e}")
            continue

    # Delay 1–2 seconds between requests
    time.sleep(random.uniform(1, 2))


# Save to CSV
with open("books_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price (£)", "Star Rating", "Category", "Availability"])
    writer.writerows(books_data)

print(f'\nScraping complete! {len(books_data)} books saved to books_data.csv')