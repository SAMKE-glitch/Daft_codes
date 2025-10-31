def register_socket_events(sio):
    """Register all socket.io event handlers."""

    @sio.event
    async def connect(sid, environ):
        print(f"Client connected: {sid}")
        await sio.emit("notification", {"message": "Welcome to the real-time API!"}, to=sid)

    @sio.event
    async def disconnect(sid):
        print(f"Client disconnected: {sid}")

    @sio.on("new_task")
    async def handle_new_task(sid, data):
        """Handle event from frontend when a new task is created."""
        print(f"Received task data: {data}")
        await sio.emit("notification", {"message": f"Task '{data['title']}' created successfully"})
