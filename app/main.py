from fastapi import FastAPI
from app.routes import blog

app = FastAPI()
app.include_router(blog.router, prefix="/blogs", tags=["Blogs"])
