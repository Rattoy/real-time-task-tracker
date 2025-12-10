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
- Schedular for background jobs

### Run locally
- git clone https://github.com/Rattoy/real-time-task-tracker.git
- cd real-time-task-tracker //getting inside the folder.
- python -m venv venv //configures the VM.
- .\venv\Scripts\activate //enables the VM.
- pip install -r requirements.txt //installing the libraries.
- uvicorn app.main:app --reload //starting the server.
