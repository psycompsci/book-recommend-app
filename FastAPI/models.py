from sqlalchemy import Boolean, Column, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)

class Book(Base):
    __tablename__ = 'books'

    isbn = Column(String(20), primary_key=True, index=True)
    title = Column(String(150))
    author = Column(String(100))
    year = Column(String(4))


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