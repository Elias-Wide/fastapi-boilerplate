# FastAPI Boilerplate

A clean, production-ready FastAPI boilerplate for building RESTful APIs with SQLAlchemy, Alembic migrations, authentication, and structured application layers.

## Repository Schema

## Source Folder Structure

- `src/`
  - `Dockerfile` - Docker image build instructions for the app
  - `main.py` - FastAPI application entry point
  - `config.py` - application configuration and environment loading
  - `conftest.py` - pytest fixtures and test configuration for source code
  - `__init__.py` - package initialization

  - `api/`
    - `__init__.py`
    - `endpoints/`
      - `__init__.py`
      - `v1/`
        - `__init__.py`
        - `routers.py` - API router registration for version 1
        - `users.py` - user-related API endpoints

  - `core/`
    - `__init__.py`
    - `logging.py` - logging setup
    - `messages.py` - application messages and constants
    - `constants/`
      - `__init__.py`
      - `core.py` - core constants
      - `users.py` - user-related constants
    - `exceptions/`
      - `__init__.py`
      - `base.py` - base exception classes
      - `handlers.py` - exception handlers
      - `mappers.py` - exception mappers
      - `api/`
        - `__init__.py`
        - `base.py`
        - `users.py`
      - `services/`
        - `__init__.py`
        - `users.py`
    - `messagesfd/`
      - `__init__.py`
      - `database.py`
      - `api/`
        - `__init__.py`
        - `base.py`
      - `db/`
        - `__init__.py`
        - `base.py`
      - `services/`
        - `__init__.py`

  - `db/`
    - `__init__.py`
    - `database.py` - database connection and session setup
    - `db_manager.py` - database session management utilities

  - `dependencies/`
    - `__init__.py`
    - `db_manager.py` - dependency providers for DB manager
    - `users.py` - route dependency helpers for user endpoints

  - `migrations/`
    - `__init__.py`
    - `env.py` - Alembic environment script
    - `README` - Alembic migration notes
    - `script.py.mako` - Alembic migration template
    - `versions/`
      - `__init__.py`
      - `e711e87b5daa_init.py` - initial database migration

  - `models/`
    - `__init__.py`
    - `users.py` - SQLAlchemy user model

  - `repositories/`
    - `__init__.py`
    - `auth.py` - authentication repository logic
    - `base.py` - base repository functionality
    - `users.py` - user data access repository

  - `schemas/`
    - `__init__.py`
    - `tokens.py` - token request/response schemas
    - `users.py` - user request/response schemas

  - `services/`
    - `__init__.py`
    - `base.py` - base service classes
    - `users.py` - user service business logic
    - `auth/`
      - `__init__.py`
      - `auth.py` - authentication business rules
      - `security.py` - security utilities
      - `tokens.py` - token generation and validation


## Notes

- The repository is organized for a clean separation between API routes, business logic, data access, and database migrations.
- The `src/` folder contains the main application code, while root files manage environment, packaging, and deployment.
- Use this structure as the base for adding new endpoints, services, and data models.