from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session, joinedload
from models import Base, User, Post
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import List

# Database configuration (Fixed connection string)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@postgres/dbname"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# FastAPI initialization
app = FastAPI()

# Pydantic models for API input/output
class UserCreate(BaseModel):
    name: str
    email: str

class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int

class UserWithPosts(BaseModel):
    id: int
    name: str
    email: str
    posts: List[PostCreate] = []

    class Config:
        orm_mode = True

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD Operations
@app.post("/users/", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/posts/", response_model=PostCreate)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = Post(title=post.title, content=post.content, user_id=post.user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@app.get("/users/{user_id}", response_model=UserCreate)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/posts/{post_id}", response_model=PostCreate)
def get_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@app.get("/users/{user_id}/posts", response_model=List[PostCreate])
def get_user_posts(user_id: int, db: Session = Depends(get_db)):
    db_posts = db.query(Post).filter(Post.user_id == user_id).all()
    return db_posts

# ✅ New: Get Users with Posts (JOIN Query)
@app.get("/users_with_posts", response_model=List[UserWithPosts])
def get_users_with_posts(db: Session = Depends(get_db)):
    users = db.query(User).options(joinedload(User.posts)).all()
    return users

# ✅ Improved Swagger UI Documentation
from fastapi.openapi.utils import get_openapi

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Backend API",
        version="1.0.0",
        description="API for managing Users and Posts",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
