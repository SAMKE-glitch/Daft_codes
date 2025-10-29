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
