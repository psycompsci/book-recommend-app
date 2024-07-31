from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated, List
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

PORT_NUMBER = 3000

# implement CORS origins; React on localhost port 3000
origins = [
    #"http://localhost:" + str(PORT_NUMBER), 
    "*",

]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

#pydantic models
class UserBase(BaseModel):
    username: str

class BookBase(BaseModel):
    book_id: int
    title: str
    authors: str
    original_publication_year: float
    average_rating: float

class BookModel(BookBase):
    book_id: int

    class Config:
        orm_mode = True


# create dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() # Close the connection to the database regardless of whether the request was successful or not

# create annotation for database for dependency injection
db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict()) #deserialize? the user object
    db.add(db_user)
    db.commit()

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first() # get the user from the database, validate if user exists
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/books/", response_model=BookModel)
async def create_book(book: BookBase, db: db_dependency):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books", response_model=List[BookModel])
async def read_books(db: db_dependency):
    books = db.query(models.Book).all()
    if books is None:
        raise HTTPException(status_code=404, detail="Books not found")
    return books

# for searching by book-id
@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int, db: db_dependency):
    book = db.query(models.Book).filter(models.Book.book_id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
