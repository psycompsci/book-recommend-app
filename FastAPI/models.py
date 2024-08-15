from sqlalchemy import Boolean, Column, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))

class Book(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    authors = Column(String(1000))
    original_publication_year = Column(Float)
    average_rating = Column(Float)
    image_url = Column(String(255))
    book_desc = Column(String(7000))
    genres = Column(String(500))
    isbn = Column(String(15), unique=True)
    isbn13 = Column(Float, unique=True)
    language_code = Column(String(10))
    pages = Column(Integer)
    books_count = Column(Integer)


"""class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    price = Column(Float)
    user_id = Column(Integer)"""
"""
 # doesn't have primary key? user id nor isbn values are unique to table
class Ratings(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, index=True)
    isbn = Column(String(20))
    rating = Column(Integer)
    """