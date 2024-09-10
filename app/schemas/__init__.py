from pydantic import UUID4, BaseModel, EmailStr
from typing import List, Literal, Optional
from uuid import UUID
from datetime import datetime

from app.models import UserRole


class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: UserRole


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(UserBase):
    user_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True


class GoodsDescriptionBase(BaseModel):
    description_text: str


class GoodsDescriptionCreate(GoodsDescriptionBase):
    pass


class GoodsDescriptionUpdate(GoodsDescriptionBase):
    pass


class GoodsDescriptionResponse(GoodsDescriptionBase):
    description_id: UUID
    user_id: UUID
    upload_date: datetime

    class Config:
        from_attributes = True


class SearchResultBase(BaseModel):
    hs_code: str
    similarity_score: float


class SearchResultCreate(SearchResultBase):
    description_id: UUID


class SearchResultResponse(SearchResultBase):
    result_id: UUID
    search_date: datetime

    class Config:
        from_attributes = True


class FeedbackBase(BaseModel):
    feedback_text: str
    expected_values: List[str]


class FeedbackCreate(FeedbackBase):
    goods_description_id: UUID4


class FeedbackResponse(FeedbackBase):
    feedback_id: UUID4
    user_id: UUID4

    class Config:
        from_attributes = True
