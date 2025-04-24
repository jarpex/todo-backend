from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import auth, todo

app = FastAPI(title="ToDo App")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://192.168.1.160:30082",
    "http://api.todo.jarpex.ru",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(todo.router, prefix="/api/v1/todos", tags=["todos"])