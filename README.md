# FastAPI Departments Tree

A production-ready FastAPI application for managing department trees, built with SQLAlchemy, Pydantic, Alembic, and Docker.

---

## 📂 Project Structure

```text
src/
├── api/                    # Endpoints and routing
│   ├── exceptions/         # API error mappers
│   └── v1/
│       ├── routers.py      # Version 1 router registration
│       └── users.py        # User endpoints
├── core/                   # Global configuration and constants
│   ├── constants/          # Application constants (core.py, users.py)
│   ├── logging.py          # Logging setup
│   └── messages.py         # Application text messages and constants
├── database/               # Database infrastructure and session setup
│   ├── db/                 # Connection management (database.py, db_manager.py)
│   └── services/           # DB-specific helper utilities
├── dependencies/           # FastAPI dependency injection providers
│   ├── db_manager.py       # DB session dependencies
│   └── users.py            # User route dependency helpers
├── exceptions/             # Global error handling exception classes
│   ├── base.py             # Base exception classes
│   └── handlers.py         # FastAPI exception handlers
├── migrations/             # Alembic database migrations
│   ├── versions/           # Migration history scripts
│   └── env.py              # Alembic environment setup script
├── models/                 # SQLAlchemy ORM models
│   └── users.py            # User database model
├── repositories/           # Data access layer (Encapsulated DB queries)
│   ├── auth.py             # Authentication data logic
│   ├── base.py             # Base repository functionality
│   └── users.py            # User data access repository
├── schemas/                # Pydantic data validation schemas
│   ├── tokens.py           # Token request/response structures
│   └── users.py            # User request/response structures
├── services/               # Core business logic layer
│   ├── auth/               # Security, tokens, and rules (security.py, tokens.py)
│   ├── base.py             # Base service classes
│   └── users.py            # User business rules execution
├── config.py               # Application settings and environment loading
├── conftest.py             # Pytest fixtures and test configuration
├── Dockerfile              # Docker image build instructions
└── main.py                 # FastAPI application entry point
```

---

## 🛠️ Getting Started

### 1. Clone the Repository
```bash
git clone git@github.com:Elias-Wide/fastapi_departments_tree.git
cd fastapi_departments_tree
```

### 2. Configure Environment Variables
Create your local environment file by copying the template:
```bash
cp .env.example .env
```
*(Make sure to open `.env` and configure your database credentials and `SECRET_KEY`).*

---

## 🚀 Option A: Running with Docker (Recommended)

### Prerequisites
Ensure you have [Docker](https://docker.com) and [Docker Compose](https://docker.com) installed.

### Start the Application
Run the following command to build the image and start all services:
```bash
docker compose up --build
```
> ℹ️ **Note:** The containers are configured to automatically execute Alembic database migrations and boot up the FastAPI server upon startup.

### Useful Docker Commands
* **Run in Background:** `docker compose up --build -d`
* **View Logs:** `docker compose logs -f`
* **Stop Services:** `docker compose down`
* **Run Tests:** `docker compose exec app poetry run pytest`

---

## 💻 Option B: Running Locally (Development Mode)

### Prerequisites
* Python 3.12+ installed
* [Poetry](https://python-poetry.org) installed
* A running PostgreSQL database instance

### 1. Install Dependencies
Install all required packages and set up the virtual environment using Poetry:
```bash
poetry install
```

### 2. Run Database Migrations
Apply the existing Alembic migrations to set up your database schema:
```bash
poetry run alembic upgrade head
```

### 3. Start the FastAPI Server
Launch the application locally inside the Poetry environment:
```bash
poetry run uvicorn src.main:app --reload
```

### Useful Local Commands
* **Run Tests:** `poetry run pytest`
* **Create New Migration:** `poetry run alembic revision --autogenerate -m "migration_name"`
* **Activate Shell:** `poetry shell`

---

## 🔍 API Documentation

Once the application is running (either via Docker or Locally), you can explore and test the endpoints directly using the built-in interactive documentation:

* **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
