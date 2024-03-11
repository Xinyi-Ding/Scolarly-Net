import pytest
import pytest_asyncio
from mongoengine import connect

from backend.app.db.config import MONGO_TEST_URI
from backend.app.intergration.catalog_access import ArticleCRUD
from backend.app.services.models import ArticleVO, ArticleFilter


@pytest_asyncio.fixture(scope="module")
async def db_connection():
    """
    Setup: Connect to the test database
    """
    connect(host=MONGO_TEST_URI, alias="test", uuidRepresentation='standard')  # Connect to your test database


# Fixture to create an instance of ArticleCRUD
@pytest_asyncio.fixture(scope="module")
def article_crud():
    return ArticleCRUD()


# Combined test function for all CRUD operations of Article
@pytest.mark.asyncio
def test_article_crud_operations(article_crud):
    # Create an article
    article_vo_create = ArticleVO(
        title="Test Article",
        abstract="This is a test article",
        publisher="Test Publisher",
        date="2024-01-01",
        issn="1234-5678",
        eissn="8765-4321",
        volume="1",
        issue="1",
        page="1-10",
        doi="10.1000/xyz123",
        meeting="Test Conference",
        file_path="/path/to/article.pdf",
        type="Journal Article",
        container_title="Test Journal"
    )
    created_article = article_crud.create(article_vo_create)
    assert created_article.title == "Test Article"
    assert created_article.abstract == "This is a test article"

    # Search by filter (using the title)
    filter_obj = ArticleFilter(title="Test Article")
    search_results = article_crud.search_by_filter(filter_obj)
    assert len(search_results) == 1
    assert search_results[0].title == "Test Article"
    assert search_results[0].abstract == "This is a test article"

    # Update article by filter (change abstract)
    update_filter_obj = ArticleFilter(article_id=created_article.article_id)
    article_vo_update = ArticleVO(
        title="Updated Test Article",  # Ensure this is a string
        abstract="This is an updated test article",
        publisher="Updated Test Publisher",
        date="2025-01-01",
        issn="1234-5678",
        eissn="8765-4321",
        volume="2",
        issue="1",
        page="11-20",
        doi="10.1000/xyz123",
        meeting="Updated Test Conference",
        file_path="/path/to/updated_article.pdf",  # Ensure this field is included
        type="Journal Article",
        container_title="Test Journal"
    )
    update_results = article_crud.update_by_filter(update_filter_obj, article_vo_update)
    assert update_results is not None
    assert len(update_results) == 1
    assert update_results[0].abstract == "This is an updated test article"

    # Get by filter to verify update
    verify_update_results = article_crud.get_by_filter(update_filter_obj)
    assert verify_update_results is not None
    assert len(verify_update_results) == 1
    assert verify_update_results[0].abstract == "This is an updated test article"

    # Delete article by filter
    delete_filter_obj = ArticleFilter(title="Updated Test Article")
    delete_success = article_crud.delete_by_filter(delete_filter_obj)
    assert delete_success

    # Verify deletion
    verify_delete_results = article_crud.get_by_filter(delete_filter_obj)
    assert verify_delete_results is None or len(verify_delete_results) == 0
