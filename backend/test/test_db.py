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
async def article(db_connection) -> Article:
    """
    Setup: Create a new Article object
    @param db_connection: None - The database connection
    @return: Article - The created article
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
async def citing_article(db_connection=db_connection) -> Article:
    """
    Setup: Create a new Article object to represent the citing article
    @param db_connection: None - The database connection
    @return: Article - The created article
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
async def cited_article(db_connection) -> Article:
    """
    Setup: Create a new Article object to represent the cited article
    @param db_connection: None - The database connection
    @return: Article - The created article
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
async def author(db_connection) -> Author:
    """
    Setup: Create a new Author object
    @param db_connection: None - The database connection
    @return: Author - The created author
    """
    test_author = Author(family_name="Doe", given_name="John", email="john.doe@example.com")
    test_author.save()

    # Yield the setup object to be used by the test
    yield test_author

    # Teardown: Clean up any created data after the test finishes
    test_author.delete()


@pytest_asyncio.fixture
async def topic(db_connection) -> Topic:
    """"
    Setup: Create a new Topic object
    @param db_connection: None - The database connection
    @return: Topic - The created topic
    """
    test_topic = Topic(name="Test Topic")
    test_topic.save()

    yield test_topic

    test_topic.delete()


@pytest_asyncio.fixture
async def institution(db_connection) -> Institution:
    """
    Setup: Create a new Institution object
    @param db_connection: None - The database connection
    @return: Institution - The created institution
    """
    test_institution = Institution(name="Test Institution")
    test_institution.save()

    # Yield the setup object to be used by the test
    yield test_institution

    # Teardown: Clean up any created data after the test finishes
    test_institution.delete()


@pytest_asyncio.fixture
async def department(db_connection, institution):
    """
    Setup: Create a new Department object
    @param db_connection: None - The database connection
    @param institution: Institution - The institution to associate with the department
    @return: Department - The created department
    """
    test_department = Department(name="Test Department", institution=institution)
    test_department.save()

    yield test_department

    test_department.delete()


@pytest_asyncio.fixture
async def parent_topic(db_connection)-> Topic:
    """
    Setup: Create a new Topic object for the parent topic
    @param db_connection: None - The database connection
    @return: Topic - The created topic
    """
    # Setup: Create a new Topic object for the parent topic
    parent = Topic(name="Parent Topic")
    parent.save()

    # Yield the setup object to be used by the test
    yield parent

    # Teardown: Clean up any created data after the test finishes
    parent.delete()


@pytest_asyncio.fixture
async def child_topic(db_connection)-> Topic:
    """
    Setup: Create a new Topic object for the child topic
    @param db_connection: None - The database connection
    @return: Topic - The created topic
    """
    # Setup: Create a new Topic object for the child topic
    child = Topic(name="Child Topic")
    child.save()

    # Yield the setup object to be used by the test
    yield child

    # Teardown: Clean up any created data after the test finishes
    child.delete()


@pytest_asyncio.fixture
async def new_institution(db_connection)-> Institution:
    """
    Setup: Create a new Institution object for testing updates
    @param db_connection: None - The database connection
    @return: Institution - The created institution
    """
    new_inst = Institution(name="New Test Institution")
    new_inst.save()

    yield new_inst

    new_inst.delete()


@pytest_asyncio.fixture
async def new_department(db_connection, new_institution)-> Department:
    """
    Setup: Create a new Department object for testing updates, associated with a new institution
    @param db_connection: None - The database connection
    @param new_institution: Institution - The new institution to associate with the department
    @return: Department - The created department
    """
    new_dept = Department(name="New Test Department", institution=new_institution)
    new_dept.save()

    yield new_dept

    new_dept.delete()


@pytest_asyncio.fixture
async def new_cited_article(db_connection)-> Article:
    """
    Setup: Create a new Article object to represent an alternative cited article for testing updates
    @param db_connection: None - The database connection
    @return: Article - The created article
    """
    new_article = Article(
        title="New Cited Article",
        publisher="New Cited Publisher",
        date="2024-03-01",
        issn="3456-7890",
        eissn="0987-6543",
        volume="3",
        issue="2",
        page="31-40",
        doi="10.1000/newcited",
        meeting="New Cited Conference",
        file_path="/path/to/new_cited_article.pdf",
        type="Review Article",  # Added new field
        container_title="New Scientific Journal"  # Added new field
    )
    new_article.save()

    yield new_article

    new_article.delete()


@pytest_asyncio.fixture
async def new_child_topic(db_connection)-> Topic:
    """
    Setup: Create a new Topic object for an alternative child topic for testing updates
    @param db_connection: None - The database connection
    @return: Topic - The created topic
    """
    new_child = Topic(name="New Child Topic")
    new_child.save()

    yield new_child

    new_child.delete()


@pytest.mark.asyncio
async def test_article_crud(article)-> None:
    """
    Test the CRUD operations for the Article model
    @param article: Article - The article to test
    @return: None
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
async def test_topic_crud(topic)-> None:
    """
    Test the CRUD operations for the Topic model
    @param topic: Topic - The topic to test
    @return: None
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
async def test_author_crud(author)-> None:
    """
    Test the CRUD operations for the Author model
    @param author: Author - The author to test
    @return: None
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
async def test_institution_crud(institution)-> None:
    """
    Test the CRUD operations for the Institution model
    @param institution: Institution - The institution to test
    @return: None
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
async def test_department_crud(db_connection, institution)-> None:
    """
    Test the CRUD operations for the Department model
    @param db_connection: None - The database connection
    @param institution: Institution - The institution to associate with the department
    @return: None
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
async def test_author_institution_crud(db_connection, author, institution, new_institution)-> None:
    """
    Test the CRUD operations for the AuthorInstitution model
    @param author: Author - The author to associate with the institution
    @param institution: Institution - The institution to associate with the author
    @param new_institution: Institution - An alternative institution for testing updates
    @return: None
    """
    # Create
    author_institution = AuthorInstitution(author=author, institution=institution)
    author_institution.save()
    assert author_institution.id is not None, "Failed to create a new AuthorInstitution relationship"

    # Read
    fetched_author_institution = AuthorInstitution.objects(id=author_institution.id).first()
    assert fetched_author_institution.author == author, "Failed to fetch the created AuthorInstitution relationship"

    # Update (e.g., changing the institution)
    author_institution.update(institution=new_institution)
    updated_author_institution = AuthorInstitution.objects(id=author_institution.id).first()
    assert updated_author_institution.institution == new_institution, "Failed to update the AuthorInstitution relationship"

    # Delete
    author_institution.delete()
    assert AuthorInstitution.objects(
        id=author_institution.id).first() is None, "Failed to delete the AuthorInstitution relationship"


@pytest.mark.asyncio
async def test_author_department_crud(db_connection, author, department, new_department) -> None:
    """
    Test the CRUD operations for the AuthorDepartment model
    @param author: Author - The author to associate with the department
    @param department: Department - The department to associate with the author
    @param new_department: Department - An alternative department for testing updates
    @return: None
    """
    # Create
    author_department = AuthorDepartment(author=author, department=department)
    author_department.save()
    assert author_department.id is not None, "Failed to create a new AuthorDepartment relationship"

    # Read
    fetched_author_department = AuthorDepartment.objects(id=author_department.id).first()
    assert fetched_author_department.author == author, "Failed to fetch the created AuthorDepartment relationship"

    # Update (e.g., changing the department)
    author_department.update(department=new_department)
    updated_author_department = AuthorDepartment.objects(id=author_department.id).first()
    assert updated_author_department.department == new_department, "Failed to update the AuthorDepartment relationship"

    # Delete
    author_department.delete()
    assert AuthorDepartment.objects(
        id=author_department.id).first() is None, "Failed to delete the AuthorDepartment relationship"


@pytest.mark.asyncio
async def test_article_citation_crud(db_connection, citing_article, cited_article, new_cited_article) -> None:
    """
    Test the CRUD operations for the ArticleCitation model
    @param citing_article: Article - The article doing the citing
    @param cited_article: Article - The article being cited
    @param new_cited_article: Article - An alternative article being cited for testing updates
    @return: None
    """
    # Create
    article_citation = ArticleCitation(citing_article=citing_article, cited_article=cited_article)
    article_citation.save()
    assert article_citation.id is not None, "Failed to create a new ArticleCitation"

    # Read
    fetched_article_citation = ArticleCitation.objects(id=article_citation.id).first()
    assert fetched_article_citation.citing_article == citing_article, "Failed to fetch the created ArticleCitation"

    # Update (e.g., changing the cited_article)
    article_citation.update(cited_article=new_cited_article)
    updated_article_citation = ArticleCitation.objects(id=article_citation.id).first()
    assert updated_article_citation.cited_article == new_cited_article, "Failed to update the ArticleCitation"

    # Delete
    article_citation.delete()
    assert ArticleCitation.objects(id=article_citation.id).first() is None, "Failed to delete the ArticleCitation"


@pytest.mark.asyncio
async def test_topic_relationship_crud(db_connection, parent_topic, child_topic, new_child_topic) ->  None:
    """
    Test the CRUD operations for the TopicRelationship model
    @param parent_topic: Topic - The parent topic
    @param child_topic: Topic - The child topic
    @param new_child_topic: Topic - An alternative child topic for testing updates
    @return: None
    """
    # Create
    topic_relationship = TopicRelationship(parent_topic=parent_topic, child_topic=child_topic)
    topic_relationship.save()
    assert topic_relationship.id is not None, "Failed to create a new TopicRelationship"

    # Read
    fetched_topic_relationship = TopicRelationship.objects(id=topic_relationship.id).first()
    assert fetched_topic_relationship.parent_topic == parent_topic, "Failed to fetch the created TopicRelationship"

    # Update (e.g., changing the child_topic)
    topic_relationship.update(child_topic=new_child_topic)
    updated_topic_relationship = TopicRelationship.objects(id=topic_relationship.id).first()
    assert updated_topic_relationship.child_topic == new_child_topic, "Failed to update the TopicRelationship"

    # Delete
    topic_relationship.delete()
    assert TopicRelationship.objects(id=topic_relationship.id).first() is None, "Failed to delete the TopicRelationship"
