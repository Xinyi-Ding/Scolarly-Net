from datetime import datetime, date

from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional


# Pydantic model for the Sequence
class SequenceVO(BaseModel):
    name: str
    value: int


# Pydantic model for the Article
class ArticleVO(BaseModel):
    id: Optional[int] = None
    title: str
    publisher: Optional[str] = None
    date: Optional[str] = None
    issn: Optional[str] = None
    eissn: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    page: Optional[str] = None
    doi: Optional[str] = None
    meeting: Optional[str] = None
    file_path: str
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


# Pydantic model for the Topic
class TopicVO(BaseModel):
    id: Optional[int] = Field(default_factory=int)
    name: str


# Pydantic model for the Author
class AuthorVO(BaseModel):
    id: Optional[int] = Field(default_factory=int)
    family_name: str
    given_name: str
    email: Optional[EmailStr] = None


# Pydantic model for the Institution
class InstitutionVO(BaseModel):
    id: Optional[int] = Field(default_factory=int)
    name: str


# Pydantic model for the Department
class DepartmentVO(BaseModel):
    id: Optional[int] = Field(default_factory=int)
    name: str
    institution_id: int  # Assuming you want to reference the Institution by its ID


# Pydantic model for Author-Institution relationship
class AuthorInstitutionVO(BaseModel):
    author_id: int  # Assuming you want to reference the Author by its ID
    institution_id: int  # Assuming you want to reference the Institution by its ID


# Pydantic model for Author-Department relationship
class AuthorDepartmentVO(BaseModel):
    author_id: int  # Assuming you want to reference the Author by its ID
    department_id: int  # Assuming you want to reference the Department by its ID


# Pydantic model for Article-Author relationship
class ArticleAuthorVO(BaseModel):
    article_id: int  # Assuming you want to reference the Article by its ID
    author_id: int  # Assuming you want to reference the Author by its ID


# Pydantic model for Article-Citation relationship
class ArticleCitationVO(BaseModel):
    citing_article_id: int  # Assuming you want to reference the citing Article by its ID
    cited_article_id: int  # Assuming you want to reference the cited Article by its ID


# Pydantic model for TopicRelationship
class TopicRelationshipVO(BaseModel):
    parent_topic_id: int  # Assuming you want to reference the parent Topic by its ID
    child_topic_id: int  # Assuming you want to reference the child Topic by its ID
