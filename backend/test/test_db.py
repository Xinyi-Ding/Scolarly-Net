import pytest
import pytest_asyncio
from backend.app.db.mongoengine_models import Article, Topic, Author, Institution, Department, AuthorInstitution, \
    AuthorDepartment, ArticleCitation, TopicRelationship
from backend.app.db.config import MONGO_TEST_URI

from mongoengine import connect


@pytest_asyncio.fixture
async def db_connection():
    """
    Setup: Connect to the test database
    """
    connect(host=MONGO_TEST_URI, alias="test", uuidRepresentation='standard')  # Connect to your test database


@pytest_asyncio.fixture
async def article(db_connection):
    """
    Setup: Create a new Article object
    """
    test_article = Article(
        title="Test Article",
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
        type="Journal Article",  # Added new field
        container_title="Test Journal"  # Added new field
    )
    test_article.save()

    yield test_article

    test_article.delete()


@pytest_asyncio.fixture
async def citing_article(db_connection):
    """
    Setup: Create a new Article object to represent the citing article
    """
    article = Article(
        title="Citing Article",
        publisher="Citing Publisher",
        date="2024-02-01",
        issn="2345-6789",
        eissn="9876-5432",
        volume="2",
        issue="1",
        page="11-20",
        doi="10.1000/citing",
        meeting="Citing Conference",
        file_path="/path/to/citing_article.pdf",
        type="Conference Paper",  # Added new field
        container_title="Annual Tech Conference"  # Added new field
    )
    article.save()

    yield article

    article.delete()


@pytest_asyncio.fixture
async def cited_article(db_connection):
    """
    Setup: Create a new Article object to represent the cited article
    """
    article = Article(
        title="Cited Article",
        publisher="Cited Publisher",
        date="2024-01-15",
        issn="1234-5678",
        eissn="8765-4321",
        volume="1",
        issue="2",
        page="21-30",
        doi="10.1000/cited",
        meeting="Cited Conference",
        file_path="/path/to/cited_article.pdf",
        type="Journal Article",  # Added new field
        container_title="Scientific Journal"  # Added new field
    )
    article.save()

    yield article

    article.delete()


@pytest_asyncio.fixture
async def author(db_connection):
    """
    Setup: Create a new Author object
    """
    test_author = Author(family_name="Doe", given_name="John", email="john.doe@example.com")
    test_author.save()

    # Yield the setup object to be used by the test
    yield test_author

    # Teardown: Clean up any created data after the test finishes
    test_author.delete()


@pytest_asyncio.fixture
async def topic(db_connection):
    """"
    Setup: Create a new Topic object
    """
    test_topic = Topic(name="Test Topic")
    test_topic.save()

    yield test_topic

    test_topic.delete()


@pytest_asyncio.fixture
async def department(db_connection, institution):
    """
    Setup: Create a new Department object
    """
    test_department = Department(name="Test Department", institution=institution)
    test_department.save()

    yield test_department

    test_department.delete()


@pytest_asyncio.fixture
async def institution(db_connection):
    """
    Setup: Create a new Institution object
    """
    test_institution = Institution(name="Test Institution")
    test_institution.save()

    # Yield the setup object to be used by the test
    yield test_institution

    # Teardown: Clean up any created data after the test finishes
    test_institution.delete()


@pytest_asyncio.fixture
async def parent_topic(db_connection):
    """
    Setup: Create a new Topic object for the parent topic
    """
    # Setup: Create a new Topic object for the parent topic
    parent = Topic(name="Parent Topic")
    parent.save()

    # Yield the setup object to be used by the test
    yield parent

    # Teardown: Clean up any created data after the test finishes
    parent.delete()


@pytest_asyncio.fixture
async def child_topic(db_connection):
    """
    Setup: Create a new Topic object for the child topic
    """
    # Setup: Create a new Topic object for the child topic
    child = Topic(name="Child Topic")
    child.save()

    # Yield the setup object to be used by the test
    yield child

    # Teardown: Clean up any created data after the test finishes
    child.delete()


@pytest.mark.asyncio
async def test_article_crud(article):
    """
    Test the CRUD operations for the Article model
    """
    # Read (The article is already created by the fixture)
    fetched_article = Article.objects(id=article.id).first()
    assert fetched_article.title == "Test Article", "Failed to fetch the created Article"

    # Update
    fetched_article.update(set__title="Updated Test Article")
    updated_article = Article.objects(id=article.id).first()
    assert updated_article.title == "Updated Test Article", "Failed to update the Article"

    # Delete is handled by the fixture


@pytest.mark.asyncio
async def test_topic_crud(topic):
    """
    Test the CRUD operations for the Topic model
    """
    # Read (The topic is already created by the fixture)
    fetched_topic = Topic.objects(id=topic.id).first()
    assert fetched_topic.name == "Test Topic", "Failed to fetch the created Topic"

    # Update
    fetched_topic.update(set__name="Updated Test Topic")
    updated_topic = Topic.objects(id=topic.id).first()
    assert updated_topic.name == "Updated Test Topic", "Failed to update the Topic"

    # Delete is handled by the fixture


@pytest.mark.asyncio
async def test_author_crud(author):
    """
    Test the CRUD operations for the Author model
    """
    # Read (The author is already created by the fixture)
    fetched_author = Author.objects(id=author.id).first()
    assert fetched_author.family_name == "Doe", "Failed to fetch the created Author"

    # Update
    fetched_author.update(set__family_name="Smith")
    updated_author = Author.objects(id=author.id).first()
    assert updated_author.family_name == "Smith", "Failed to update the Author"

    # Delete is handled by the fixture


@pytest.mark.asyncio
async def test_institution_crud(institution):
    """
    Test the CRUD operations for the Institution model
    """
    # Read (The institution is already created by the fixture)
    fetched_institution = Institution.objects(id=institution.id).first()
    assert fetched_institution.name == "Test Institution", "Failed to fetch the created Institution"

    # Update
    fetched_institution.update(set__name="Updated Test Institution")
    updated_institution = Institution.objects(id=institution.id).first()
    assert updated_institution.name == "Updated Test Institution", "Failed to update the Institution"

    # Delete is handled by the fixture


@pytest.mark.asyncio
async def test_department_crud(db_connection, institution):
    """
    Test the CRUD operations for the Department model
    """
    # Now you can use the 'institution' fixture in your test
    # Create
    department = Department(name="Computer Science", institution=institution)
    department.save()
    assert department.id is not None, "Failed to create a new Department"

    # Read
    fetched_department = Department.objects(id=department.id).first()
    assert fetched_department.name == "Computer Science", "Failed to fetch the created Department"

    # Update
    fetched_department.update(set__name="Updated Computer Science")
    updated_department = Department.objects(id=department.id).first()
    assert updated_department.name == "Updated Computer Science", "Failed to update the Department"

    # Delete is handled by the fixture


@pytest.mark.asyncio
async def test_author_institution_crud(db_connection, author, institution):
    """
    Test the CRUD operations for the AuthorInstitution model
    """
    # Create
    author_institution = AuthorInstitution(author=author, institution=institution)
    author_institution.save()
    assert author_institution.id is not None, "Failed to create a new AuthorInstitution relationship"

    # Read
    fetched_author_institution = AuthorInstitution.objects(id=author_institution.id).first()
    assert fetched_author_institution.author == author, "Failed to fetch the created AuthorInstitution relationship"

    # Update & Delete not applicable for EmbeddedDocument

    # Delete is handled by the fixture


@pytest.mark.asyncio
async def test_author_department_crud(db_connection, author, department):
    """
    Test the CRUD operations for the AuthorDepartment model
    """
    # Create
    author_department = AuthorDepartment(author=author, department=department)
    author_department.save()
    assert author_department.id is not None, "Failed to create a new AuthorDepartment relationship"

    # Read
    fetched_author_department = AuthorDepartment.objects(id=author_department.id).first()
    assert fetched_author_department.author == author, "Failed to fetch the created AuthorDepartment relationship"

    # Update & Delete not applicable for EmbeddedDocument

    # Delete is handled by the fixture


@pytest.mark.asyncio
async def test_article_citation_crud(db_connection, citing_article, cited_article):
    """
    Test the CRUD operations for the ArticleCitation model
    """
    # Create
    article_citation = ArticleCitation(citing_article=citing_article, cited_article=cited_article)
    article_citation.save()
    assert article_citation.id is not None, "Failed to create a new ArticleCitation"

    # Read
    fetched_article_citation = ArticleCitation.objects(id=article_citation.id).first()
    assert fetched_article_citation.citing_article == citing_article, "Failed to fetch the created ArticleCitation"

    # Update & Delete not applicable for this relationship

    # Delete is handled by the fixture


@pytest.mark.asyncio
async def test_topic_relationship_crud(db_connection, parent_topic, child_topic):
    """
    Test the CRUD operations for the TopicRelationship model
    """
    # Create
    topic_relationship = TopicRelationship(parent_topic=parent_topic, child_topic=child_topic)
    topic_relationship.save()
    assert topic_relationship.id is not None, "Failed to create a new TopicRelationship"

    # Read
    fetched_topic_relationship = TopicRelationship.objects(id=topic_relationship.id).first()
    assert fetched_topic_relationship.parent_topic == parent_topic, "Failed to fetch the created TopicRelationship"

    # Update & Delete not applicable for this relationship

    # Delete is handled by the fixture
