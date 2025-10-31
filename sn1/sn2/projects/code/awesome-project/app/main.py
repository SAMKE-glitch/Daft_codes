from fastapi import FastAPI
from app.controllers import item_controller
from sqlmodel import SQLModel
from app.dependencies.db_dependency import engine
import socketio
from app.sockets.socket_events import register_socket_events


# Initialize Socket.IO server
sio = socket.AsyncServer(async_mode="asgi", cors_allowed_origins="*")


# Mount FastAPI + Socket.IO together

app = FastAPI(titel="Awesome Project with Socket.IO")
app_sio = socketio.ASGIApp(sio, other_asgi_app=app)
register_socket_events(sio)

# Create DB tables
SQLModel.metadata.create_all(engine)


# Register routes (controllers)
app.include_router(item_controller.router)

"""
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
"""
