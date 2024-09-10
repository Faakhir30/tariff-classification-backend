from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from app.models import Feedback, GoodsDescription
from app.schemas import FeedbackCreate, FeedbackResponse
from app.session.db import get_db
from app.dependencies.auth import auth_dep
from typing import List
from app.models import UserRole
from app.models import User


router = APIRouter()

from .feedbackPost import create_feedback
from .feedbackGet import read_feedback, get_all_feedback
from .feedbackDelete import delete_feedback
