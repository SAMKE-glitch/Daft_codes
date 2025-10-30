from typing import Union
from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# Step 1: Dependency (simulated authentication)
def get_user():
    print("Fetching user from database...")
    return {"username": "Samke", "role": "Engineer"}

@app.get("/")
async def read_root(user: dict = Depends(get_user)):
    return {"message": f"Welcome {user['username']}!"}

@app.get("/items/{item_id}")  # ✅ added missing slash
async def read_item(item_id: int, q: Union[str, None] = None):  # ✅ fixed type hint
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

