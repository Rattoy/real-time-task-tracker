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

### OPTION 1: Run locally
- git clone https://github.com/Rattoy/real-time-task-tracker.git
- cd real-time-task-tracker 
- python -m venv venv
  For Windows:
- .\venv\Scripts\activate
  For Linux:
- source venv/bin/activate
- pip install -r requirements.txt 
- uvicorn app.main:app --reload 
  
### OPTION 2: Run With Docker
- git clone https://github.com/Rattoy/real-time-task-tracker.git
- git pull
- docker build -t real-time-task-tracker .
- docker run -p 8000:8000 real-time-task-tracker

### API Documentation
Once the server is running, you can access the API documentation to test the endpoints:
- Swagger UI (Interactive): http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Raw JSON Output: http://127.0.0.1:8000
- Run GUI: http://127.0.0.1:8000/static/GUI.html
