from fastapi import APIRouter, Depends, HTTPException
from app.services.item_service import ItemService
from app.dependencies.auth_dependency import get_user
from typing import Union
from app.models.item_model import Item


router = APIRouter()
service = ItemService()

@router.get("/")
async def read_root(user: dict = Depends(get_user)):
    return {"message": f"Welcome {user['username']}!"}


@router.get("/items/{item_id}")
def get_item(item_id: int, user: dict = Depends(get_user)):
    try:
        item = service.fetch_item(item_id)
        return {"user": user["username"], "item": item}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# Extra route: query parameter optional
@router.get("/items-query/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q":q}


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
