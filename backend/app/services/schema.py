# Pydantic model for the Response
from typing import Any, Optional
from datetime import date

from pydantic import BaseModel, Field


def to_camel(string: str) -> str:
    parts = string.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])


class ResponseSchema(BaseModel):
    code: int = 200
    msg: str = "success"
    data: list | dict | Any = None


class AuthorSchema(BaseModel):
    author_id: int = Field(None, alias="authorId")
    name: str = None
    email: str = None
    affiliation: Optional[str] = None

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class TopicSchema(BaseModel):
    topic_id: int = Field(None, alias="topicId")
    name: str = None

    # original: Optional[bool] = False

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class PaperItemSchema(BaseModel):
    article_id: int = Field(None, alias="articleId")
    title: str = None
    authors: list[AuthorSchema] = []

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class PaperResponse(ResponseSchema):
    data: list[PaperItemSchema] = []


class TopicItemSchema(BaseModel):
    topic_id: int = Field(None, alias="topicId")
    topic: str = None
    count: int = None

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class TopicResponse(ResponseSchema):
    data: list[TopicItemSchema] = []


class AuthorItemSchema(BaseModel):
    author_id: int = Field(None, alias="authorId")
    name: str = None
    count: int = None

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class AuthorResponse(ResponseSchema):
    data: list[AuthorItemSchema] = []


class SameTopicConnectionItemSchema(BaseModel):
    topic: int = None
    papers: list[int] = []


class SameTopicDataSchema(BaseModel):
    connections: list[SameTopicConnectionItemSchema] = []
    topics: list[TopicSchema] = []
    papers: list[PaperItemSchema] = []


class SameTopicResponseSchema(ResponseSchema):
    data: SameTopicDataSchema = {}


class CoAuthorConnectionItemSchema(BaseModel):
    author: int = None
    papers: list[int] = []


class CoAuthorDataSchema(BaseModel):
    connections: list[CoAuthorConnectionItemSchema] = []
    authors: list[AuthorSchema] = []
    papers: list[PaperItemSchema] = []


class CoAuthorResponseSchema(ResponseSchema):
    data: CoAuthorDataSchema = {}


class CitedConnectionItemSchema(BaseModel):
    from_paper: int = Field(None, alias="fromPaper")
    to_paper: list[int] = Field(None, alias="toPaper")

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class CitedTreeDataSchema(BaseModel):
    connections: list[CitedConnectionItemSchema]
    papers: list[PaperItemSchema]


class CitedTreeResponseSchema(ResponseSchema):
    data: CitedTreeDataSchema = {}
