import requests
from bs4 import BeautifulSoup

def scrape_first_20_books():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # The main page contains exactly 20 books
    book_pods = soup.find_all('article', class_='product_pod')
    
    # Dictionary to map text ratings to integers
    rating_mapping = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    
    extracted_books = []
    
    for pod in book_pods:
        # 1. Title
        title = pod.h3.a['title']
        
        # 2. Price (stripped of symbols and cast to float)
        price_str = pod.find('p', class_='price_color').text
        # The site often includes an 'Â£' symbol; we strip anything that isn't a digit or decimal
        clean_price = ''.join(char for char in price_str if char.isdigit() or char == '.')
        price = float(clean_price)
        
        # 3. In Stock (Boolean)
        availability = pod.find('p', class_='instock availability').text.strip()
        in_stock = "In stock" in availability
        
        # 4. Rating (Mapped to Integer 1-5)
        # The class list looks like ['star-rating', 'Three']
        rating_class = pod.p['class'][1]
        rating = rating_mapping.get(rating_class, 0)
        
        extracted_books.append({
            "title": title,
            "price": price,
            "in_stock": in_stock,
            "rating": rating
        })
        
    return extracted_books

if __name__ == "__main__":
    books = scrape_first_20_books()
    for i, book in enumerate(books, 1):
        print(f"{i}. {book}")