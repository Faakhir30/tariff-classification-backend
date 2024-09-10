import logging
from app.session.db import Base, engine
from app import models
from sqlalchemy.exc import SQLAlchemyError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def drop_all_tables():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
        logger.info("All tables dropped successfully")
    except SQLAlchemyError as e:
        logger.error(f"Error dropping tables: {str(e)}")
        raise


async def create_all_tables():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("All tables created successfully")
    except SQLAlchemyError as e:
        logger.error(f"Error creating tables: {str(e)}")
        raise


async def initialize_database():
    try:
        await drop_all_tables()
        await create_all_tables()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize database: {str(e)}")
        raise
