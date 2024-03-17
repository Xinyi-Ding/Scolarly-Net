from mongoengine import Document, connect
from mongoengine.fields import (
    StringField, IntField, DateField
)
from .config import MONGO_URI, MONGO_TEST_URI, TEST_MODE

# Establish a connection to MongoDB using the variables from config.py
if TEST_MODE:
    connect(host=MONGO_TEST_URI, uuidRepresentation='standard')
else:
    connect(host=MONGO_URI, uuidRepresentation='standard')


# Define the Sequence model to store sequence values
class Sequence(Document):
    meta = {'collection': 'sequence'}
    name = StringField(required=True, unique=True, sparse=True)
    value = IntField(required=True)

    @classmethod
    def get_next_sequence(cls, sequence_name):
        # Try to find a sequence by name
        sequence = cls.objects(name=sequence_name).first()
        if not sequence:
            # If not found, create a new sequence with value 1
            sequence = cls(name=sequence_name, value=1)
            sequence.save()
        else:
            # If found, increment the sequence value atomically
            sequence.update(inc__value=1)
            sequence.reload()  # Reload to get the updated value
        return sequence.value


# Now, we can use the `Sequence` model within the `sequence` function
def sequence(sequence_name):
    return Sequence.get_next_sequence(sequence_name)


# Article model
class Article(Document):
    # Unique identifier for each article.
    article_id = IntField(primary_key=True, default=lambda: sequence('article'))
    # The title of the article.
    title = StringField(required=True, max_length=255)
    # The abstract of the article. This field can be null.
    abstract = StringField(max_length=4000)
    # The publisher of the article. This field can be null.
    publisher = StringField(max_length=255)
    # The original date the article was written or submitted. This field can be null.
    date = DateField()
    # International Standard Serial Number of the article. This field can be null but should be unique if provided.
    issn = StringField(max_length=20, unique=True, sparse=True)
    # Electronic International Standard Serial Number. This field can be null but should be unique if provided.
    eissn = StringField(max_length=20, unique=True, sparse=True)
    # The volume in which the article was published. This field can be null.
    volume = StringField(max_length=10)
    # The issue of the volume in which the article was published. This field can be null.
    issue = StringField(max_length=10)
    # The page number(s) of the article in the publication. This field can be null.
    page = StringField(max_length=10)
    # Digital Object Identifier for the article. This field can be null but should be unique if provided.
    doi = StringField(max_length=255, unique=True, sparse=True)
    # The conference or meeting where the article was presented. This field can be null.
    meeting = StringField(max_length=255)
    # The location where the article file is stored.
    file_path = StringField(max_length=255)
    # The type of the publication (e.g., Journal Article, Conference Paper, Book, etc.). This field can be null.
    type = StringField(max_length=255)
    # The title of the container holding the publication (e.g., Journal Title, Conference Name, Book Title,
    # etc.). This field can be null.
    container_title = StringField(max_length=255)

    meta = {'collection': 'article',
            'indexes': [
                'title',
                'date',
                {'fields': ['issn'], 'unique': True},
                {'fields': ['eissn'], 'unique': True},
                {'fields': ['doi'], 'unique': True},
                {'fields': ['$title'],
                 'default_language': 'english',
                 'weights': {'title': 10}}
            ]
            }

    def clean(self):
        # Convert empty strings or other "empty" values to None for unique fields
        for field in ['issn', 'eissn', 'doi']:
            if not getattr(self, field):
                setattr(self, field, None)


# Topic model
class Topic(Document):
    # Unique identifier for each topic.
    topic_id = IntField(primary_key=True, default=lambda: sequence('topic'))
    # The name of the topic. It must be unique.
    name = StringField(required=True, max_length=200, unique=True, sparse=True)

    meta = {'collection': 'topic',
            'indexes': [
                'name',
                {'fields': ['$name'],
                 'default_language': 'english',
                 }
            ]
            }


# Author model
class Author(Document):
    # Unique identifier for each author.
    author_id = IntField(primary_key=True, default=lambda: sequence('author'))
    # The name of the author.
    name = StringField(required=True, max_length=255)
    # The email address of the author. This field can be null but should be unique if provided.
    email = StringField(unique=True, max_length=255, sparse=True)

    def clean(self):
        # Convert empty strings or other "empty" values to None for unique fields
        for field in ['email']:
            if not getattr(self, field):
                setattr(self, field, None)

    meta = {'collection': 'author',
            'indexes': [
                {
                    'fields': ['name', 'email'],
                    'unique': True
                },
                {'fields': ['$name'],
                 'default_language': 'english',
                 }
            ]
            }


# Institution model
class Institution(Document):
    # Unique identifier for each institution.
    institution_id = IntField(primary_key=True, default=lambda: sequence('institution'))
    # The name of the institution. It must be unique.
    name = StringField(required=True, max_length=255, unique=True, sparse=True)

    meta = {'collection': 'institution',
            'indexes': [
                'name',
                {'fields': ['$name'],
                 'default_language': 'english',
                 }
            ]}


# Department model
class Department(Document):
    # Unique identifier for each department.
    department_id = IntField(primary_key=True, default=lambda: sequence('department'))
    # The name of the department.
    name = StringField(required=True, max_length=255)
    # Reference to the Institution document.
    institution_id = IntField()

    meta = {'collection': 'department'}


# Author-Institution model (relationship)
class AuthorInstitution(Document):
    # Reference to the Author document; represents the many-to-many relationship between authors and institutions.
    author_id = IntField(required=True)
    # Reference to the Institution document; represents the many-to-many relationship between authors and institutions.
    institution_id = IntField(required=True)

    meta = {
        'collection': 'author_institution',
        'indexes': [
            {
                'fields': ['author_id', 'institution_id'],
                'unique': True
            },
        ]
    }


# Author-Department model (relationship)
class AuthorDepartment(Document):
    # Reference to the Author document; represents the many-to-many relationship between authors and departments.
    author_id = IntField(required=True)
    # Reference to the Department document; represents the many-to-many relationship between authors and departments.
    department_id = IntField(required=True)

    meta = {
        'collection': 'author_department',
        'indexes': [
            {
                'fields': ['author_id', 'department_id'],
                'unique': True
            },
        ]
    }


# Article-Author model (relationship)
class ArticleAuthor(Document):
    # Reference to the Article document.
    article_id = IntField(required=True)
    # Reference to the Author document.
    author_id = IntField(required=True)

    meta = {
        'collection': 'article_author',
        'indexes': [
            {
                'fields': ['article_id', 'author_id'],
                'unique': True
            },
        ]
    }


# Article-Citation model
class ArticleCitation(Document):
    # Reference to the Article document that is doing the citing.
    citing_article_id = IntField(required=True)
    # Reference to the Article document that is being cited.
    cited_article_id = IntField(required=True)

    meta = {
        'collection': 'article_citation',
        'indexes': [
            {
                'fields': ['citing_article_id', 'cited_article_id'],
                'unique': True
            },
        ]
    }


class ArticleTopic(Document):
    article_id = IntField(required=True)
    topic_id = IntField(required=True)

    meta = {
        'collection': 'article_topic',
        'indexes': [
            {
                'fields': ['article_id', 'topic_id'],
                'unique': True
            },
        ]
    }


# TopicRelationship model
class TopicRelationship(Document):
    # Reference to the Topic document that is the parent topic.
    parent_topic_id = IntField(required=True)
    # Reference to the Topic document that is the child topic.
    child_topic_id = IntField(required=True)

    meta = {
        'collection': 'topic_relationship',
        'indexes': [
            {
                'fields': ['parent_topic_id', 'child_topic_id'],
                'unique': True
            },
        ]
    }


def ensure_indexes():
    """
    Ensure that all indexes are created for the models.
    """
    Article.ensure_indexes()
    Sequence.ensure_indexes()
    Topic.ensure_indexes()
    Author.ensure_indexes()
    Institution.ensure_indexes()
    Department.ensure_indexes()
    AuthorInstitution.ensure_indexes()
    AuthorDepartment.ensure_indexes()
    ArticleAuthor.ensure_indexes()
    ArticleCitation.ensure_indexes()
    ArticleTopic.ensure_indexes()
    TopicRelationship.ensure_indexes()


# Ensure indexes are created
# ensure_indexes()
