from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.session.db import get_session
from app.models.item import Item

router = APIRouter()

@router.post("/items/", response_model=Item)
def create_item(item: Item, session: Session = Depends(get_session)):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@router.get("/items/", response_model=list[Item])
def read_items(session: Session = Depends(get_session)):
    items = session.exec(select(Item)).all()
    return items
