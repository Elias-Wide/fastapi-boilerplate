# FastAPI Boilerplate

This is a production-ready template for building REST APIs with FastAPI. It provides a clean, layered architecture designed for creating flexible web applications. The boilerplate includes database integration, a built-in User Service, async repositories, Pydantic schemas, JWT-based authentication, and user management endpoints out of the box.

---

## Project Structure

src/
├── api/                  # Endpoints and routing
│   ├── exceptions/       # API error mappers
│   └── v1/
│       ├── routers.py    # Version 1 router registration
│       └── users.py      # User endpoints
├── core/                 # Global configuration and constants
│   ├── constants/        # Application constants (core.py, users.py)
│   ├── logging.py        # Logging setup
│   └── messages.py       # Application text messages and constants
├── database/             # Database infrastructure and session setup
│   ├── db/               # Connection management (database.py, db_manager.py)
│   └── services/         # DB-specific helper utilities
├── dependencies/         # FastAPI dependency injection providers
│   ├── db_manager.py     # DB session dependencies
│   └── users.py          # User route dependency helpers
├── exceptions/           # Global error handling exception classes
│   ├── base.py           # Base exception classes
│   └── handlers.py       # FastAPI exception handlers
├── migrations/           # Alembic database migrations
│   ├── versions/         # Migration history scripts
│   └── env.py            # Alembic environment setup script
├── models/               # SQLAlchemy ORM models
│   └── users.py          # User database model
├── repositories/         # Data access layer (Encapsulated DB queries)
│   ├── auth.py           # Authentication data logic
│   ├── base.py           # Base repository functionality
│   └── users.py          # User data access repository
├── schemas/              # Pydantic data validation schemas
│   ├── tokens.py         # Token request/response structures
│   └── users.py          # User request/response structures
├── services/             # Core business logic layer
│   ├── auth/             # Security, tokens, and rules (security.py, tokens.py)
│   ├── base.py           # Base service classes
│   └── users.py          # User business rules execution
├── config.py             # Application settings and environment loading
├── conftest.py           # Pytest fixtures and test configuration
├── Dockerfile            # Docker image build instructions
└── main.py               # FastAPI application entry point

---

## Getting Started

### 1. Clone the Repository
Clone the repository and enter the project directory:
```bash
git clone git@github.com:Elias-Wide/fastapi_departments_tree.git
cd fastapi_departments_tree
```

### 2. Configure the Project Metadata
Before installing dependencies, open the `pyproject.toml` file in the root directory. Update the project metadata fields to match your new application requirements:
* change the `name` field to your application name
* update the `version`, `description`, and `authors` fields as needed

### 3. Configure Environment Variables
Create your local environment file by copying the provided template:
```bash
cp .env.example .env
```
Open the `.env` file and configure your database credentials, application name, and the `SECRET_KEY` variable.

---

## Option A: Running with Docker (Recommended)

### Prerequisites
Ensure you have Docker and Docker Compose installed on your system.

### Start the Application
Run the following command to build the image and start all services:
```bash
docker compose up --build
```
Note: The containers are configured to automatically execute Alembic database migrations and boot up the FastAPI server upon startup.

### Useful Docker Commands
* Run in Background: `docker compose up --build -d`
* View Logs: `docker compose logs -f`
* Stop Services: `docker compose down`
* Run Tests: `docker compose exec app poetry run pytest`

---

## Option B: Running Locally (Development Mode)

### Prerequisites
* Python 3.12+ installed
* Poetry installed
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
* Run Tests: `poetry run pytest`
* Create New Migration: `poetry run alembic revision --autogenerate -m "migration_name"`
* Activate Shell: `poetry shell`

---

## API Documentation

Once the application is running either via Docker or locally, you can explore and test the endpoints directly using the built-in interactive documentation:
* Swagger UI: http://localhost:8000/docs
* ReDoc: http://localhost:8000/redoc

