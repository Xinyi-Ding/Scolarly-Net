# Pydantic model for the Response
from typing import Any, Optional
from datetime import date

from pydantic import BaseModel


class ResponseSchema(BaseModel):
    code: int = 200
    msg: str = "success"
    data: list | dict | Any = None


class AuthorSchema(BaseModel):
    id: int = None
    name: str = None
    email: str = None
    affiliation: Optional[str] = None


class TopicSchema(BaseModel):
    id: int = None
    name: str = None
    # original: Optional[bool] = False


class PaperItemSchema(BaseModel):
    id: int = None
    title: str = None
    authors: list[AuthorSchema] = []


class PaperResponse(ResponseSchema):
    data: list[PaperItemSchema] = []


class TopicItemSchema(BaseModel):
    id: int = None
    topic: str = None
    count: int = None


class TopicResponse(ResponseSchema):
    data: list[TopicItemSchema] = []


class AuthorItemSchema(BaseModel):
    id: int = None
    name: str = None
    count: int = None


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


class DashboardItemSchema(BaseModel):
    id: int = None
    title: str = None
    authors: list[str] = []
    affiliations: list[str] = []
    date: date = None
    doi: str = None
    keywords: list[str] = []
    references: int = None


class DashboardResponseSchema(ResponseSchema):
    data: DashboardItemSchema = None


class CitedConnectionItemSchema(BaseModel):
    from_paper: int
    to_paper: list[int]


class CitedTreeDataSchema(BaseModel):
    connections: list[CitedConnectionItemSchema]
    papers: list[PaperItemSchema]


class CitedTreeResponseSchema(ResponseSchema):
    data: CitedTreeDataSchema = {}
