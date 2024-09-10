import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.session import db
from app.session.models_init import create_all_tables, drop_all_tables
from sqlalchemy.exc import SQLAlchemyError

from app.routers.auth.authRouter import router as auth_router
from app.routers.description.descriptionRouter import router as discription_router
from app.routers.feedback.feedbackRouter import router as feedback_router
from app.routers.search.searchRouter import router as search_router

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def initialize_database():
    try:
        logger.info("Dropping all tables...")
        await drop_all_tables()
        logger.info("Creating all tables...")
        await create_all_tables()
        logger.info("Database initialized successfully")
    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemy error during database initialization: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during database initialization: {str(e)}")
        raise


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up the application...")
    try:
        await initialize_database()
    except Exception as e:
        logger.error(f"Failed to initialize database: {str(e)}")
        # You might want to exit the application here if database init fails
        # import sys
        # sys.exit(1)


app.include_router(auth_router, prefix="/auth")
app.include_router(discription_router, prefix="/descriptions")
app.include_router(feedback_router, prefix="/feedback")
app.include_router(search_router, prefix="/search")


# Root route
@app.get("/")
def read_root():
    return "Server is running"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
