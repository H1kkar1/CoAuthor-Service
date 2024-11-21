from fastapi import FastAPI
from app.post.router import post_router

app = FastAPI()

app.include_router(post_router)
