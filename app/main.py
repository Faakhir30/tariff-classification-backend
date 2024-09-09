import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.session import db
from app.session.models_init import create_all_tables, drop_all_tables

from app.routers.auth.authRouter import router as auth_router
from app.routers.discriptions.discriptionRouter import router as discription_router
from app.routers.feedback.feedbackRouter import router as feedback_router
from app.routers.search.searchRouter import router as search_router


app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def init_db():
    await drop_all_tables()
    await create_all_tables()


app.include_router(auth_router, prefix="/auth")
app.include_router(discription_router, prefix="/descriptions")
app.include_router(feedback_router, prefix="/feedback")
app.include_router(search_router, prefix="/search")


# Root route
@app.get("/")
def read_root():
    return "Server is running"
