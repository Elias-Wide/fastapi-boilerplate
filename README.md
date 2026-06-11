# FastAPI Auth & User Management Service

A production-ready FastAPI application for user management and authentication, built with SQLAlchemy, Pydantic, Alembic, Poetry, and Docker.

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

## 📐 Architecture & Layer Description

The project strictly follows a layered architectural pattern to ensure clean separation of concerns, high testability, and maintainability.

### 1. API & Routing Layer (`src/api/`)
* **Purpose:** Handles incoming HTTP requests, defines route paths, and returns HTTP responses.
* **Logic:** Does not contain business logic. It relies on **Dependency Injection** (`src/dependencies/`) to inject required services, handles validation errors using dedicated API exception mappers (`src/api/exceptions/`), and routes requests to the appropriate Service methods.

### 2. Business Logic Layer (`src/services/`)
* **Purpose:** The core of the application where business rules, constraints, and operation logic live.
* **Logic:** Services manipulate domain concepts (e.g., executing user business rules or authentication logic inside `src/services/auth/`). They orchestrate the workflow by communicating with the Data Access Layer (Repositories) and utilizing security utilities (`src/services/security.py`).

### 3. Data Access Layer (`src/repositories/`)
* **Purpose:** Encapsulates all raw database operations and queries.
* **Logic:** Implements the Repository Pattern (`src/repositories/base.py`). All SQLAlchemy queries are strictly restricted to this layer. This prevents business services from depending directly on the underlying database client or structure, making it easier to mock or switch databases later.

### 4. Data Validation & Models Layer (`src/schemas/` & `src/models/`)
* **Schemas (`src/schemas/`):** Built with Pydantic. Used for validating data payloads entering the application (Request) and serialization before returning data to the client (Response). Includes configurations for user inputs and token responses.
* **Models (`src/models/`):** Built with SQLAlchemy ORM. Represents the actual database tables schema (e.g., `users.py`).

### 5. Dependency Injection (`src/dependencies/`)
* **Purpose:** Manages the lifecycle of resources needed by the API routers.
* **Logic:** Provides clean helper utilities like injecting database sessions (`db_manager.py`) or handling specific user-route dependency prerequisites (`users.py`) in a decoupled manner.

### 6. Infrastructure & Core Configuration (`src/database/`, `src/core/`, `src/exceptions/`)
* **Database Management:** Handles sessions setup (`database.py`) and connection persistence utilities.
* **Global Exceptions:** A centralized place for internal app exceptions (`base.py`) and FastAPI custom global error handlers (`handlers.py`).
* **Core:** Stores systemic essentials including centralized configuration management (`config.py`), logging setups (`logging.py`), and localized constants/messages.

---

## 🛠️ Configuration

### Configure Environment Variables
Create your local environment file by copying the template in the project root directory:
```bash
cp .env.example .env
```
*(Make sure to open `.env` and configure your database credentials, environment variables, and `SECRET_KEY`).*

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
* Python 3.10+ installed
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
