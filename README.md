# Real-time Task Tracker
A task management REST API built with FastAPI and SQLAlchemy.

### Tech stack
- Python 3.11
- FastAPI (REST API)
- SQLAlchemy ORM + Alembic (migrations)
- SQLite / PostgreSQL (configurable)
- Pytest (tests)

### Features
- Task CRUD (create, read, update, delete)
- User models and DB relationships
- Modular structure: models, schemas, CRUD, API routes
- Alembic migrations for schema management

### Run locally
git clone ...
cd task-tracker
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
