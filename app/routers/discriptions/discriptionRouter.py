from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from uuid import UUID
from typing import List

from app.session.db import get_db
from app.models import GoodsDescription
from app.models import User
from app.schemas import (
    GoodsDescriptionCreate,
    GoodsDescriptionUpdate,
    GoodsDescriptionResponse,
)
from app.dependencies.auth import auth_dep

router = APIRouter()

from .discriptionPost import create_goods_description
from .discriptionPut import update_goods_description
from .discriptionGet import get_goods_descriptions, get_goods_description
from .discriptionDelete import delete_goods_description
