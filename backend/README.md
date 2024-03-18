# Backend Service

## Overview

This backend service is structured to support various functionalities including database operations, service integration, API routing, and core business logic implementation. It is designed with modularity and scalability in mind.

## Directory Structure

- `app/`: Main application directory.
  - `db/`: Contains database configurations and models.
    - `config.py`: Database configuration settings.
    - `mongoengine_models.py`: Definitions of database models using MongoEngine.
    - `__init__.py`: Initializes the database module.
  - `integration/`: Handles external service integration.
    - `catalog_access.py`: Access layer for catalog services.
    - `__init__.py`: Initializes the integration module.
  - `routers/`: API routes for the application.
    - `analysis_api.py`: Endpoints related to analysis operations.
    - `catalog_api.py`: Endpoints for catalog management.
    - `dependencies.py`: Dependency definitions for API routes.
    - `__init__.py`: Initializes the routers module.
  - `services/`: Core business logic and service layer.
    - `Extractors/`: Contains extractors for different types of data.
    - `Parser/`:` Contains parsers for different types of data.
    - `analysis.py`: Analysis service logic.
    - `catalog.py`: Catalog service logic.
    - `models.py`: Service layer models.
    - `schema.py`: Schema definitions for routers layer.
    - `__init__.py`: Initializes the services module.
  - `main.py`: Entry point of the application.
  - `__init__.py`: Initializes the application module.
- `test/`: Contains unit tests.
  - `test_main.py`: Test cases for the main application.
  - `__init__.py`: Initializes the test module.
- `README.md`: This file.
- `requirements.txt`: Project dependencies.

## Installation

1. Clone the repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Configure your environment variables as necessary.

## Running the Application

1. Enter the `backend` directory.
    ```
    cd backend
    ```
2. (Optional) Cancel TEST MODE (default is True) by setting the environment variable `TEST_MODE` to `False`:
    ```
    export TEST_MODE=False
    ```
3. Execute the following command:
    ```
    python -m app.main
    ```

## Testing

1/ To run tests, execute:

```
python -m pytest
```
