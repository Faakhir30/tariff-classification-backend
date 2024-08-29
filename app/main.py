import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from app.routers.auth import router as authRouter
from app.routers.item import router as itemRouter
from app.session.db import engine  # Import engine
from app.models.item import Item   # Import models

api_app = FastAPI()

# Add CORS middleware
api_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
api_app.include_router(authRouter, prefix="/auth")
api_app.include_router(itemRouter, prefix="/items")


# Create tables on startup
@api_app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# Root route
@api_app.get("/")
def read_root():
    return "Server is running"
