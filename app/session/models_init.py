from app.session.db import Base, engine

from app import models

from sqlalchemy.ext.asyncio import create_async_engine


async def drop_all_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def create_all_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
