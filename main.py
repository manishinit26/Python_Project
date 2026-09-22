from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import BookDatabaseManager

app = FastAPI(title="Book Data Pipeline API")
db = BookDatabaseManager()

# Pydantic model to validate incoming data for POST and PUT requests
class BookPayload(BaseModel):
    title: str
    price: float
    in_stock: bool
    rating: int

@app.get("/books")
def get_all_books():
    """Retrieve all stored books."""
    return db.get_all_books()

@app.get("/books/{book_id}")
def get_single_book(book_id: int):
    """Retrieve a single book by ID."""
    book = db.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books")
def create_new_book(book: BookPayload):
    """Create a new book entry."""
    new_id = db.create_book(book.title, book.price, book.in_stock, book.rating)
    return {"message": "Book created successfully", "id": new_id, "book": book.model_dump()}

@app.put("/books/{book_id}")
def update_existing_book(book_id: int, book: BookPayload):
    """Update an existing book entry."""
    success = db.update_book(book_id, book.title, book.price, book.in_stock, book.rating)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book updated successfully", "id": book_id}

@app.delete("/books/{book_id}")
def delete_book_entry(book_id: int):
    """Delete a book entry by ID."""
    success = db.delete_book(book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}