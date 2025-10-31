from fastapi import FastAPI
from sqlmodel import SQLModel
from app.controllers import item_controller
from app.dependencies.db_dependency import engine
import socketio
from app.sockets.socket_events import register_socket_events
from fastapi.staticfiles import StaticFiles


# Initialize Socket.IO server
sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")

# Initialize FastAPI app
app = FastAPI(titel="Awesome Project with Socket.IO")

# Mount FastAPI + Socket.IO together
app_sio = socketio.ASGIApp(sio, other_asgi_app=app)

# Register all socket events
register_socket_events(sio)

# Create DB tables (if not exist)
SQLModel.metadata.create_all(engine)


# Register routes (controllers)
app.include_router(item_controller.router)

# Serve static files (frontend)
app.mount("/socket", StaticFiles(directory="app/static", html=True), name="static")

# This ensures both FastAPI & Socket.IO routes work
app = app_sio
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
