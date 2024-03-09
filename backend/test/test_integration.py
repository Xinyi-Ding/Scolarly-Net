import pytest
from backend.app.services.models import ArticleVO
from backend.app.intergration.catalog_access import create_article, get_article, update_article, delete_article

# Data for article creation, all fields populated
initial_article_data = ArticleVO(
    title="Test Title",
    publisher="Test Publisher",
    date="2024-01-01",
    issn="1234-5678",
    eissn="8765-4321",
    volume="1",
    issue="1",
    page="100-200",
    doi="10.1000/testdoi",
    meeting="Test Meeting",
    file_path="/path/to/article",
    type="Research",
    container_title="Test Journal"
)

# Data for article update, might only change a few fields
updated_article_data = ArticleVO(
    title="Updated Title",
    publisher="Updated Publisher",
    date="2024-01-01",
    issn="2234-5678",
    eissn="8766-4321",
    volume="2",
    issue="2",
    page="200-300",
    doi="10.2000/testdoi",
    meeting="Updated Meeting",
    file_path="/path/updated/article",
    type="Review",
    container_title="Updated Journal"
)


@pytest.mark.asyncio
async def test_article_crud():
    """
    Test creating, reading, updating, and deleting an article in the catalog.
    This test flows through each CRUD operation sequentially.
    """

    # Create
    created_article = create_article(initial_article_data)
    assert created_article.title == initial_article_data.title  # add other assertions

    # Read
    retrieved_article = get_article(created_article.id)
    assert retrieved_article.title == created_article.title  # add other assertions

    # Update
    updated_article = update_article(created_article.id, updated_article_data)
    assert updated_article.title == updated_article_data.title  # add other assertions

    # Delete
    result = delete_article(created_article.id)
    assert result is True

    # Verify Deletion
    deleted_article = get_article(created_article.id)
    assert deleted_article is None
