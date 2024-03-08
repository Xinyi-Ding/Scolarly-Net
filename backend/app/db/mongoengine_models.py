from mongoengine import Document, connect
from mongoengine.fields import (
    StringField, IntField, DateField, EmailField, ReferenceField
)
from backend.app.db.config import MONGO_URI

# Establish a connection to MongoDB using the variables from config.py
connect(host=MONGO_URI, uuidRepresentation='standard')


# Define the Sequence model to store sequence values
class Sequence(Document):
    meta = {'collection': 'sequence'}
    name = StringField(required=True, unique=True)
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
    meta = {'collection': 'article'}
    # Unique identifier for each article.
    id = IntField(primary_key=True, default=lambda: sequence('article'))
    # The title of the article.
    title = StringField(required=True, max_length=255)
    # The publisher of the article. This field can be null.
    publisher = StringField(max_length=255)
    # The original date the article was written or submitted. This field can be null.
    date = DateField()
    # International Standard Serial Number of the article. This field can be null but should be unique if provided.
    issn = StringField(max_length=20, unique=True)
    # Electronic International Standard Serial Number. This field can be null but should be unique if provided.
    eissn = StringField(max_length=20, unique=True)
    # The volume in which the article was published. This field can be null.
    volume = StringField(max_length=10)
    # The issue of the volume in which the article was published. This field can be null.
    issue = StringField(max_length=10)
    # The page number(s) of the article in the publication. This field can be null.
    page = StringField(max_length=10)
    # Digital Object Identifier for the article. This field can be null but should be unique if provided.
    doi = StringField(max_length=255, unique=True)
    # The conference or meeting where the article was presented. This field can be null.
    meeting = StringField(max_length=255)
    # The location where the article file is stored.
    file_path = StringField(required=True, max_length=255)
    # The type of the publication (e.g., Journal Article, Conference Paper, Book, etc.). This field can be null.
    type = StringField(max_length=255)
    # The title of the container holding the publication (e.g., Journal Title, Conference Name, Book Title,
    # etc.). This field can be null.
    container_title = StringField(max_length=255)


# Topic model
class Topic(Document):
    meta = {'collection': 'topic'}
    # Unique identifier for each topic.
    id = IntField(primary_key=True, default=lambda: sequence('topic'))
    # The name of the topic. It must be unique.
    name = StringField(required=True, max_length=100, unique=True)


# Author model
class Author(Document):
    meta = {'collection': 'author'}
    # Unique identifier for each author.
    id = IntField(primary_key=True, default=lambda: sequence('author'))
    # The family name of the author.
    family_name = StringField(required=True, max_length=255)
    # The given name of the author.
    given_name = StringField(required=True, max_length=255)
    # The email address of the author. This field can be null but should be unique if provided.
    email = EmailField(unique=True, max_length=255)


# Institution model
class Institution(Document):
    meta = {'collection': 'institution'}
    # Unique identifier for each institution.
    id = IntField(primary_key=True, default=lambda: sequence('institution'))
    # The name of the institution. It must be unique.
    name = StringField(required=True, max_length=255, unique=True)


# Department model
class Department(Document):
    meta = {'collection': 'department'}
    # Unique identifier for each department.
    id = IntField(primary_key=True, default=lambda: sequence('department'))
    # The name of the department.
    name = StringField(required=True, max_length=255)
    # Reference to the Institution document.
    institution = ReferenceField(Institution, required=True)


# Author-Institution model (relationship)
class AuthorInstitution(Document):
    # Reference to the Author document; represents the many-to-many relationship between authors and institutions.
    author = ReferenceField(Author, required=True)
    # Reference to the Institution document; represents the many-to-many relationship between authors and institutions.
    institution = ReferenceField(Institution, required=True)


# Author-Department model (relationship)
class AuthorDepartment(Document):
    # Reference to the Author document; represents the many-to-many relationship between authors and departments.
    author = ReferenceField(Author, required=True)
    # Reference to the Department document; represents the many-to-many relationship between authors and departments.
    department = ReferenceField(Department, required=True)


# Article-Author model (relationship)
class ArticleAuthor(Document):
    # Reference to the Article document.
    article = ReferenceField(Article, required=True)
    # Reference to the Author document.
    author = ReferenceField(Author, required=True)


# Article-Citation model
class ArticleCitation(Document):
    meta = {'collection': 'article_citation'}
    # Reference to the Article document that is doing the citing.
    citing_article = ReferenceField(Article, required=True, dbref=True)
    # Reference to the Article document that is being cited.
    cited_article = ReferenceField(Article, required=True, dbref=True)


# TopicRelationship model
class TopicRelationship(Document):
    meta = {'collection': 'topic_relationship'}
    # Reference to the Topic document that is the parent topic.
    parent_topic = ReferenceField(Topic, required=True, dbref=True)
    # Reference to the Topic document that is the child topic.
    child_topic = ReferenceField(Topic, required=True, dbref=True)
