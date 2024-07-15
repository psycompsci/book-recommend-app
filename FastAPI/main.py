from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

class ItemBase(BaseModel):
    title: str
    price: float
    user_id: int

class UserBase(BaseModel):
    username: str

class RatingBase(BaseModel):
    id: int
    isbn: str
    rating: int

# create dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() # Close the connection to the database regardless of whether the request was successful or not

# create annotation for database for dependency injection
db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict()) #deserialize? the user object --> 
    db.add(db_user)
    db.commit()

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first() # get the user from the database, validate if user exists
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user