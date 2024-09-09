import enum
import uuid
from sqlalchemy import Column, Enum, String, DateTime, ForeignKey, Text, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from app.session.db import Base


class UserRole(enum.Enum):
    ADMIN = "admin"
    USER = "user"


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.USER)
    created_at = Column(DateTime, default=datetime.utcnow)

    descriptions = relationship("GoodsDescription", back_populates="user")


class GoodsDescription(Base):
    __tablename__ = "goods_descriptions"

    description_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    description_text = Column(Text, nullable=False)
    upload_date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="descriptions")
    search_results = relationship("SearchResult", back_populates="description")


class SearchResult(Base):
    __tablename__ = "search_results"

    result_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    description_id = Column(
        UUID(as_uuid=True),
        ForeignKey("goods_descriptions.description_id"),
        nullable=False,
    )
    hs_code = Column(String, nullable=False)
    similarity_score = Column(Float, nullable=False)
    search_date = Column(DateTime, default=datetime.utcnow)

    description = relationship("GoodsDescription", back_populates="search_results")
