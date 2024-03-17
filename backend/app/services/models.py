import re
import warnings
from dataclasses import dataclass
from datetime import datetime, date
from pydantic import BaseModel, Field, validator
from typing import Optional, List, AnyStr


# Pydantic model for the Sequence
class SequenceVO(BaseModel):
    name: str
    value: int


# Pydantic model for the Article
class ArticleVO(BaseModel):
    article_id: Optional[int] = Field(None)
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
        # If the date is None, or the input is None, simply return None
        if v is None or v == '':
            return None

        if isinstance(v, (datetime, date)):
            # If the input is a datetime or date object, convert it to a string in 'YYYY-MM-DD' format.
            return v.strftime('%Y-%m-%d')

        # Define a comprehensive list of date formats to try
        date_formats = [
            '%Y-%m-%d',  # ISO 8601 format
            '%d-%m-%Y',  # Common UK/EU format
            '%m-%d-%Y',  # Common US format
            '%Y/%m/%d',  # ISO 8601 alternative format
            '%d/%m/%Y',  # Common UK/EU alternative format
            '%m/%d/%Y',  # Common US alternative format
            '%Y-%m',  # Four-digit year and month
            '%m-%Y',  # Month and four-digit year
            '%Y/%m',  # Four-digit year and month (alternative)
            '%m/%Y',  # Month and four-digit year (alternative)
            '%Y',  # Four-digit year
            '%y',  # Two-digit year
            '%b %d %Y',  # Abbreviated month name, e.g., Jan 02 2021
            '%B %d %Y',  # Full month name, e.g., January 02 2021
            '%d %b %Y',  # Day first, abbreviated month name
            '%d %B %Y',  # Day first, full month name
            '%b %d, %Y',  # Abbreviated month name with comma, e.g., Jan 02, 2021
            '%B %d, %Y',  # Full month name with comma, e.g., January 02, 2021
            '%d-%b-%Y',  # Day first, abbreviated month name with dashes
            '%d-%B-%Y',  # Day first, full month name with dashes
            '%d %b, %Y',  # Day first, abbreviated month name with comma
            '%d %B, %Y',  # Day first, full month name with comma
            '%Y %b %d',  # Year first, abbreviated month name
            '%Y %B %d',  # Year first, full month name
            '%b %Y',  # Abbreviated month name and year
            '%B %Y',  # Full month name and year
            '%d-%b',  # Day and abbreviated month
            '%d-%B',  # Day and full month
            '%b-%d',  # Abbreviated month and day
            '%B-%d',  # Full month and day
            '%Y-%b-%d',  # Year, abbreviated month, and day
            '%Y-%B-%d',  # Year, full month, and day
            '%d-%b-%Y',  # Day, abbreviated month, and year
            '%d-%B-%Y',  # Day, full month, and year
        ]

        # Try to parse the date string using each format
        for date_format in date_formats:
            try:
                # Attempt to parse the date string
                parsed_date = datetime.strptime(v, date_format)

                # If successful, return the date string in 'YYYY-MM-DD' format
                return parsed_date.strftime('%Y-%m-%d')
            except ValueError:
                # If parsing fails, continue to try the next format
                continue

        # If none of the formats match, set date to None and issue a warning
        warnings.warn(f"Date '{v}' does not match any of the recognized formats. Setting 'date' to None.")
        return None

    @validator('doi', pre=True, allow_reuse=True)
    def validate_doi(cls, v):
        if v is None or v == '':
            return None

        # Regular expression for validating a DOI
        doi_regex = re.compile(r'^10.\d{4,9}/[-._;()/:A-Za-z0-9]+$')

        if not doi_regex.match(v):
            # If the DOI doesn't match the regex, issue a warning and return None
            warnings.warn(f"DOI '{v}' does not match the standard DOI format. Setting 'doi' to None.")
            return None

        return v

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class ArticleFilter(ArticleVO):
    article_id: Optional[int] = None
    title: Optional[str] = None
    file_path: Optional[str] = None


# Pydantic model for the Topic
class TopicVO(BaseModel):
    topic_id: Optional[int] = Field(None)
    name: str

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class TopicFilter(TopicVO):
    topic_id: Optional[int] = None
    name: Optional[str] = None


# Pydantic model for the Author
class AuthorVO(BaseModel):
    author_id: Optional[int] = Field(None)
    name: str
    email: Optional[str] = None

    @validator('email', pre=True, allow_reuse=True)
    def validate_email(cls, v):
        if v is None or v == '':
            return None

        # Regular expression for validating an Email
        email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        # If the email is not empty or None, try matching against the regex
        if not email_regex.match(v):
            # If the email doesn't match the regex, issue a warning and return None
            warnings.warn(f"Provided email '{v}' is not a valid email format. Setting 'email' to None.")
            return None

        # If the email matches the regex, return it as is
        return v

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class AuthorFilter(AuthorVO):
    author_id: Optional[int] = None
    name: Optional[str] = None


# Pydantic model for the Institution
class InstitutionVO(BaseModel):
    institution_id: Optional[int] = Field(None)
    name: str

    class Config:
        orm_mode = True  # Enable ORM mode to allow the model to work with ORM objects.


class InstitutionFilter(InstitutionVO):
    institution_id: Optional[int] = None
    name: Optional[str] = None


# Pydantic model for the Department
class DepartmentVO(BaseModel):
    department_id: Optional[int] = Field(None)
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

    def dict(self):
        pass


# VO class for Artical, representing the entire article including metadata, content, authors, and references
@dataclass
class ParseArticalVO:
    metadata: ParseMetadataVO  # The metadata of the article
    content: ParseContentVO  # The content of the article
    authors: List[ParseAuthorVO]  # A list of authors of the article
    references: List[ParseReferenceVO]  # A list of references cited in the article

    @staticmethod
    def from_dict(data: dict):
        return ParseArticalVO(
            metadata=ParseMetadataVO(**data['metadata']),
            content=ParseContentVO(**data['content']),
            authors=[ParseAuthorVO(**author) for author in data['authors']],
            references=[ParseReferenceVO(**reference) for reference in data['references']]
        )
