from dataclasses import dataclass
from datetime import datetime, date
from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List, AnyStr


# Pydantic model for the Sequence
class SequenceVO(BaseModel):
    name: str
    value: int


# Pydantic model for the Article
class ArticleVO(BaseModel):
    article_id: Optional[int] = Field(default_factory=int)
    title: str
    abstract: Optional[str] = None
    publisher: Optional[str] = None
    date: Optional[str] = None
    issn: Optional[str] = None
    eissn: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    page: Optional[str] = None
    doi: Optional[str] = None
    meeting: Optional[str] = None
    file_path: Optional[str] = None
    type: Optional[str] = None
    container_title: Optional[str] = None

    @validator('date', pre=True, allow_reuse=True)
    def validate_date(cls, v):
        if isinstance(v, (datetime, date)):
            # If the input is a datetime or date object, convert it to a string in 'YYYY-MM-DD' format.
            v = v.strftime('%Y-%m-%d')

        if v is not None:
            try:
                # Validate that the string is in 'YYYY-MM-DD' format.
                datetime.strptime(v, '%Y-%m-%d')
            except ValueError:
                # If the string is not in the correct format, raise a ValueError.
                raise ValueError('Date must be in YYYY-MM-DD format')
        return v  # Return the validated date string

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class ArticleFilter(ArticleVO):
    article_id: Optional[int] = None
    title: Optional[str] = None
    file_path: Optional[str] = None


# Pydantic model for the Topic
class TopicVO(BaseModel):
    topic_id: Optional[int] = Field(default_factory=int)
    name: str

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class TopicFilter(TopicVO):
    topic_id: Optional[int] = None
    name: Optional[str] = None


# Pydantic model for the Author
class AuthorVO(BaseModel):
    author_id: Optional[int] = Field(default_factory=int)
    name: str
    email: Optional[EmailStr] = None

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class AuthorFilter(AuthorVO):
    author_id: Optional[int] = None
    name: Optional[str] = None


# Pydantic model for the Institution
class InstitutionVO(BaseModel):
    institution_id: Optional[int] = Field(default_factory=int)
    name: str

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class InstitutionFilter(InstitutionVO):
    institution_id: Optional[int] = None
    name: Optional[str] = None


# Pydantic model for the Department
class DepartmentVO(BaseModel):
    department_id: Optional[int] = Field(default_factory=int)
    name: str
    institution_id: Optional[int] = None  # Assuming you want to reference the Institution by its ID

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class DepartmentFilter(DepartmentVO):
    department_id: Optional[int] = None
    name: Optional[str] = None


# Pydantic model for Author-Institution relationship
class AuthorInstitutionVO(BaseModel):
    author_id: int  # Assuming you want to reference the Author by its ID
    institution_id: int  # Assuming you want to reference the Institution by its ID

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class AuthorInstitutionFilter(AuthorInstitutionVO):
    author_id: Optional[int] = None
    institution_id: Optional[int] = None


# Pydantic model for Author-Department relationship
class AuthorDepartmentVO(BaseModel):
    author_id: int  # Assuming you want to reference the Author by its ID
    department_id: int  # Assuming you want to reference the Department by its ID

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class AuthorDepartmentFilter(AuthorDepartmentVO):
    author_id: Optional[int] = None
    department_id: Optional[int] = None


# Pydantic model for Article-Author relationship
class ArticleAuthorVO(BaseModel):
    article_id: int  # Assuming you want to reference the Article by its ID
    author_id: int  # Assuming you want to reference the Author by its ID

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class ArticleAuthorFilter(ArticleAuthorVO):
    article_id: Optional[int] = None
    author_id: Optional[int] = None


# Pydantic model for Article-Author relationship
class ArticleTopicVO(BaseModel):
    article_id: int  # Assuming you want to reference the Article by its ID
    topic_id: int  # Assuming you want to reference the Topic by its ID

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class ArticleTopicFilter(ArticleTopicVO):
    article_id: Optional[int] = None
    topic_id: Optional[int] = None


# Pydantic model for Article-Citation relationship
class ArticleCitationVO(BaseModel):
    citing_article_id: int  # Assuming you want to reference the citing Article by its ID
    cited_article_id: int  # Assuming you want to reference the cited Article by its ID

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class ArticleCitationFilter(ArticleCitationVO):
    citing_article_id: Optional[int] = None
    cited_article_id: Optional[int] = None


# Pydantic model for TopicRelationship
class TopicRelationshipVO(BaseModel):
    parent_topic_id: int  # Assuming you want to reference the parent Topic by its ID
    child_topic_id: int  # Assuming you want to reference the child Topic by its ID

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class TopicRelationshipFilter(TopicRelationshipVO):
    parent_topic_id: Optional[int] = None
    child_topic_id: Optional[int] = None


# VO class for Metadata, representing the metadata of an article
@dataclass
class ParseMetadataVO:
    title: str  # The title of the article
    doi: str  # Digital Object Identifier for the article
    publisher: str  # The publisher of the article
    journal: str  # The journal where the article is published
    published_date: str  # The publication date of the article


# VO class for Content, representing the main content of an article
@dataclass
class ParseContentVO:
    abstract: str  # The abstract of the article
    keywords: List[AnyStr]  # A list of keywords associated with the article


# VO class for Author, representing an author of the article
@dataclass
class ParseAuthorVO:
    name: str  # The name of the author
    affiliation: str  # The affiliation of the author
    email: Optional[str]  # The email address of the author, which is optional


# VO class for Reference, representing a reference cited in the article
@dataclass
class ParseReferenceVO:
    authors: List[str]  # A list of authors of the reference
    title: str  # The title of the reference
    type: str  # The type of the reference (e.g., journal article, book)
    container_title: str  # The title of the container holding the reference (e.g., journal name)
    doi: str  # Digital Object Identifier for the reference
    published_date: str  # The publication date of the reference


# VO class for Artical, representing the entire article including metadata, content, authors, and references
@dataclass
class ParseArticalVO:
    metadata: ParseMetadataVO  # The metadata of the article
    content: ParseContentVO  # The content of the article
    authors: List[ParseAuthorVO]  # A list of authors of the article
    references: List[ParseReferenceVO]  # A list of references cited in the article
