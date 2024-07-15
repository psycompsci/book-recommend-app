from sqlalchemy import Boolean, Column, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    price = Column(Float)
    user_id = Column(Integer)

class Ratings(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, index=True)
    isbn = Column(String(20))
    rating = Column(Integer)