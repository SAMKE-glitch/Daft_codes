from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import Union, List
from app.dependencies.db_dependency import get_session
from app.models.item_model import Item
from app.services.item_service import ItemService


router = APIRouter()

# Root route (welcome message)
@router.get("/")
async def read_root():
    return {"message": "Welcome to Awesome Project!"}

# Get single item by ID
@router.get("/items/{item_id}")
def get_item(item_id: int, session: Session = Depends(get_session)):
    service = ItemService(session)
    try:
        item = service.fetch_item(item_id)
        return item
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Get item with optional query parameter
@router.get("/items-query/{item_id}")
def read_item(item_id: int, q:Union[str, None] = None, session: Session = Depends(get_session)):
    service = ItemService(session)
    try: 
        item = service.fetch_item(item_id)
        return {"item": item, "query": q}
    except ValueError as e:
        raise HTTPEception(status_code=404, detail=str(e))

# Create new item
@router.post("/items/", response_model=Item)
def create_item(item: Item, session: Session = Depends(get_session)):
    service = ItemService(session)
    return service.create_item(item)


# Update item by ID
@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item, session: Session = Depends(get_session)):
    service = ItemService(session)
    existing_item = service.fetch_item(item_id)
    existing_item.name = item.name
    existing_item.price = item.price
    existing_item.is_offer = item.is_offer
    session.add(existing_item)
    session.commit()
    session.refresh(existing_item)
    return existing_item

# Delete item by ID
@router.delete("/items/{item_id}")
def delete_tem(item_id: int, session: Session = Depends(get_session)):
    service = ItemService(session)
    existing_item = service.fetch_item(item_id)
    session.delete(existing_item)
    session.commit()
    return {"detail": f"Item {item_id} deleted successfully."}


# Get all items (optional: for testing)
@router.get("/items/", response+model=List[Item])
def get_all_items(session: Session = Depends(get_session)):
    items = Session.exec(select(Item)).all()
    return items


