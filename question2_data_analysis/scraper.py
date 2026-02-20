import requests
from bs4 import BeautifulSoup
import csv
import time
import random
import os

BASE_URL = 'http://books.toscrape.com/catalogue/page-{}.html'

raw_data_path = 'question2_data_analysis/data/raw_books_data.csv'

headers = {
    'User-Agent': 'Mozilla/5.0'
}

class Scrpaer:    

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

    # Scrape 3 pages (100 books minimum)
    
    @staticmethod
    def scrape_data():
        ''' scrape and save raw data '''
        books_data = []

        for page in range(1, 3):
            url = BASE_URL.format(page)
            print(f'Scraping Page {page}...')

            response = Scrpaer.get_page(url)

            if response is None:
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            books = soup.find_all("article", class_="product_pod")

            for book in books:
                try:
                    title = book.h3.a["title"]
                    price = book.find("p", class_="price_color").text.strip()
                    availability = book.find("p", class_="instock availability").text.strip()
                    star_tag = book.find("p", class_="star-rating")
                    star_rating = star_tag.get("class")[1] if star_tag else "N/A"
                    #rating = extract_star_rating(" ".join(star_class))

                    # Get book detail page to extract category
                    detail_url = book.h3.a["href"]
                    detail_url = "http://books.toscrape.com/catalogue/" + detail_url

                    detail_response = Scrpaer.get_page(detail_url)
                    if detail_response:
                        detail_soup = BeautifulSoup(detail_response.text, "html.parser")
                        category = detail_soup.find("ul", class_="breadcrumb").find_all("a")[2].text
                    else:
                        category = "N/A"

                    books_data.append([title, price, star_rating, category, availability])

                except Exception as e:
                    print(f"Error processing book: {e}")
                    continue

            # Delay 1–2 seconds between requests
            time.sleep(random.uniform(1, 2))

        # Save to CSV
        with open(raw_data_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Price (£)", "Star Rating", "Category", "Availability"])
            writer.writerows(books_data)

        print(f'\nScraping complete! {len(books_data)} books saved to raw_books_data.csv')