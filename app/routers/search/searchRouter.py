from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from app.models import SearchResult, GoodsDescription
from app.schemas import SearchResultCreate, SearchResultResponse
from app.session.db import get_db
from app.dependencies.auth import auth_dep
from app.schemas import SearchResultBase
from app.models import User

router = APIRouter()
