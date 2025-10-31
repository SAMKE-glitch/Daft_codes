# My first typer project
## Directory structure example
```
app/
├── main.py              # Entry point
├── core/
│   ├── config.py        # Settings, environment variables
│   └── security.py      # Auth utilities
├── api/
│   ├── routes/
│   │   ├── users.py     # Route handlers
│   │   ├── items.py
│   │   └── __init__.py
│   └── dependencies.py  # Shared dependencies (e.g., DB session)
├── models/
│   └── user.py          # SQLAlchemy or Pydantic models
├── db/
│   └── session.py       # Database connection
└── tests/
    └── test_users.py

```
## FastAPI “MVC-style” Project Architecture
```
awesome-project/
│
├── app/
│   ├── __init__.py
│   ├── main.py                 # Entry point (like Spring Boot Application.java)
│   ├── controllers/            # Controllers (routes)
│   │   ├── __init__.py
│   │   └── item_controller.py
│   ├── services/               # Business logic
│   │   ├── __init__.py
│   │   └── item_service.py
│   ├── repositories/           # Data access logic (DB or API)
│   │   ├── __init__.py
│   │   └── item_repository.py
│   ├── models/                 # Pydantic models (data schemas)
│   │   ├── __init__.py
│   │   └── item_model.py
│   └── dependencies/           # Dependency injection functions
│       ├── __init__.py
│       └── auth_dependency.py
│
└── requirements.txt


```

## Updated Project Structure with Socket.IO
```
awesome-project/
│
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI entrypoint
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── item_controller.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── item_service.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── item_repository.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── item_model.py
│   ├── sockets/                   # <── NEW: real-time communication handlers
│   │   ├── __init__.py
│   │   └── socket_events.py       # defines @sio.event functions
│   └── dependencies/
│       ├── __init__.py
│       └── db_dependency.py

```
