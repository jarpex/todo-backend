from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import auth, todo

app = FastAPI(title="ToDo App")

origins = [
    "https://todo.jarpex.com",   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "PUT", "PATCH", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(todo.router, prefix="/api/v1/todos", tags=["todos"])