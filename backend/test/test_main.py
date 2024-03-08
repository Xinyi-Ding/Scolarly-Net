import pytest
from httpx import AsyncClient
from backend.app.main import app  # Import the FastAPI application instance


# Test for the root endpoint "/"
@pytest.mark.asyncio
async def test_root():
    # Asynchronously send a GET request to the root endpoint and assert response
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"uri": "/"}


# Test for the "/catalog/" endpoint
@pytest.mark.asyncio
async def test_catalog_root():
    # Asynchronously send a GET request to the "/catalog/" endpoint and assert response
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/catalog/")
    assert response.status_code == 200
    assert response.json() == {"uri": "/catalog"}


# Test for the "/analysis/" endpoint
@pytest.mark.asyncio
async def test_analysis_root():
    # Asynchronously send a GET request to the "/analysis/" endpoint and assert response
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/analysis/")
    assert response.status_code == 200
    assert response.json() == {"uri": "/analysis"}
