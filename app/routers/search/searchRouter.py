from fastapi.responses import JSONResponse
from app.schemas import SearchRequestBase
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

from .searchPost import create_search_result
from .searchGet import read_search_result, get_all_search_results
from .searchDelete import delete_search_result
from .searchPut import update_search_result
