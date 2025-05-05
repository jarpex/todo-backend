import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import auth, todo

# Detect environment
IS_PRODUCTION = os.getenv("ENVIRONMENT") == "production"

# Disable docs in production
app = FastAPI(
    title="ToDo App",
    docs_url=None if IS_PRODUCTION else "/docs",
    redoc_url=None if IS_PRODUCTION else "/redoc",
    openapi_url=None if IS_PRODUCTION else "/openapi.json",
)

# CORS
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://192.168.1.160:30081",
    "http://todo.jarpex.com",
    "https://todo.jarpex.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "PUT", "PATCH", "DELETE"],
    allow_headers=["Content-Type", "Authorization", "Origin", "Accept"],
    expose_headers=["Content-Type", "Authorization"],
)

# Routes
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(todo.router, prefix="/api/v1/todos", tags=["todos"])