from fastapi import FastAPI, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    price: float
    genre: str
    author: Optional[str] = None

class UpdateBook(BaseModel):
    title: Optional[str] = None
    price: Optional[float] = None
    genre: Optional[str] = None
    author: Optional[str] = None

library = {}

@app.get("/get-book/{book_id}", status_code=200)
def get_book(book_id: int = Path(..., description="The ID of the item you'd like to view")):
    if book_id in library:
        return library[book_id]
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/get-book-by-title", status_code=200)
def get_book_by_title(title: str = Query(..., title="Title", description="Name of Book")):
    for book_id in library:
        if library[book_id].title == title:
            return library[book_id]
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/create-book/{book_id}", status_code=201)
def create_book(book_id: int, book: Book):
    if book_id in library:
        raise HTTPException(status_code=400, detail="Book ID already exists")
    library[book_id] = book
    return library[book_id]

@app.put("/update-book/{book_id}", status_code=200)
def update_book(book_id: int, book: UpdateBook):
    if book_id not in library:
        raise HTTPException(status_code=404, detail="Book ID does not exist")

    if book.title is not None:
        library[book_id].title = book.title

    if book.price is not None:
        library[book_id].price = book.price
    
    if book.genre is not None:
        library[book_id].genre = book.genre
    
    if book.author is not None:
        library[book_id].author = book.author

    return library[book_id]

@app.delete("/delete-book", status_code=200)
def delete_book(book_id: int = Query(..., description="The ID of the item to delete")):
    if book_id not in library:
        raise HTTPException(status_code=404, detail="Book ID does not exist")

    del library[book_id]
    return {"Success": "Book deleted"}