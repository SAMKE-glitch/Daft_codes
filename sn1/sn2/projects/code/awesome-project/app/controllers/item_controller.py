from fastapi import APIRouter, Depends, HTTPException
from app.services.item_service import ItemService
from app.dependencies.auth_dependency import get_user


router = APIRouter()

service = ItemService()

@router.get("/items/{item_id}")
def get_item(item_id: int, user: dict = Depends(get_user)):
    try:
        item = service.fetch_item(item_id)
        return {"user": user["username"], "item": item}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
