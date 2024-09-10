from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/mydatabase"
# DATABASE_URL = "postgresql+asyncpg://postgres:admin@172.18.0.2:5432/mydatabase"
DATABASE_URL = "postgresql+asyncpg://postgres:admin@localhost:5432/mydatabase"


engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)

Base = declarative_base()


async def get_db():
    async with SessionLocal() as session:
        yield session
