import sqlite3
from web_scraper import scrape_first_20_books

class BookDatabaseManager:
    def __init__(self, db_name="books.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                price REAL NOT NULL,
                in_stock BOOLEAN NOT NULL,
                rating INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    # CREATE
    def create_book(self, title, price, in_stock, rating):
        self.cursor.execute("""
            INSERT INTO books (title, price, in_stock, rating)
            VALUES (?, ?, ?, ?)
        """, (title, price, in_stock, rating))
        self.conn.commit()
        return self.cursor.lastrowid

    # READ ALL
    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        # Convert tuples to list of dictionaries for easier API handling later
        columns = [column[0] for column in self.cursor.description]
        return [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    # READ ONE
    def get_book_by_id(self, book_id):
        self.cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        row = self.cursor.fetchone()
        if row:
            columns = [column[0] for column in self.cursor.description]
            return dict(zip(columns, row))
        return None

    # UPDATE
    def update_book(self, book_id, title, price, in_stock, rating):
        self.cursor.execute("""
            UPDATE books
            SET title = ?, price = ?, in_stock = ?, rating = ?
            WHERE id = ?
        """, (title, price, in_stock, rating, book_id))
        self.conn.commit()
        return self.cursor.rowcount > 0

    # DELETE
    def delete_book(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def close(self):
        self.conn.close()

# Test and Populate Database
if __name__ == "__main__":
    db = BookDatabaseManager()
    
    # Check if database is already populated to avoid duplicates on re-runs
    existing_books = db.get_all_books()
    if not existing_books:
        print("Database is empty. Scraping books and populating database...")
        scraped_books = scrape_first_20_books()
        for book in scraped_books:
            db.create_book(book['title'], book['price'], book['in_stock'], book['rating'])
        print("20 books successfully inserted into books.db!")
    else:
        print(f"Database already contains {len(existing_books)} books.")
    
    # Test a read operation
    sample_book = db.get_book_by_id(1)
    print(f"\nSample Book (ID 1): {sample_book}")
    
    db.close()