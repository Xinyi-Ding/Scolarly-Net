# Pydantic model for the Response
from typing import Any, Optional
from datetime import date

from pydantic import BaseModel


class ResponseVO(BaseModel):
    code: int
    msg: str
    data: list


class AuthorVO(BaseModel):
    id: int
    name: str
    email: str
    affiliation: Optional[str] = None


class PaperItemVO(BaseModel):
    id: int
    title: str
    authors: list[AuthorVO]


class PaperResponse(ResponseVO):
    data: list[PaperItemVO]


class TopicItemVO(BaseModel):
    id: int
    topic: str
    count: int


class TopicResponse(ResponseVO):
    data: list[TopicItemVO]


class AuthorItemVO(BaseModel):
    id: int
    name: str
    count: int


class AuthorResponse(ResponseVO):
    data: list[AuthorItemVO]


class TopicConnectionItemVO(BaseModel):
    id: int
    name: str
    original: bool


class ConnectionItemVO(BaseModel):
    topic: int
    papers: list[int]


class TopicConnectionResponseVO(ResponseVO):
    data: dict[str, Any]


class SameTopicPaperItemVO(PaperItemVO):
    original: Optional[bool] = False


class SameTopicResponseVO(ResponseVO):
    data: dict[str, Any]


class DashboardItemVO(BaseModel):
    id: int
    title: str
    authors: list[str]
    affiliations: list[str] = []  # 可以使用空列表作为默认值
    date: date
    doi: str
    keywords: list[str]
    references: int


class DashboardResponseVO(ResponseVO):
    data: DashboardItemVO


class CoAuthorItemVO(BaseModel):
    id: int
    name: str
    original: Optional[bool] = False  # Optional field to indicate if this is the original author


class CoAuthorConnectionItemVO(BaseModel):
    author: int
    papers: list[int]


class CoAuthorResponseVO(ResponseVO):
    data: dict[str, Any]  # Use a flexible type to accommodate the nested structure of "co-author" data


class CitedConnectionItemVO(BaseModel):
    from_paper: int  # Renamed from 'from' to 'from_paper' to avoid using Python reserved keyword
    to: list[int]


class CitedPaperItemVO(PaperItemVO):
    original: Optional[bool] = False  # Add an optional field to indicate the original paper


class CitedTreeResponseVO(ResponseVO):
    data: dict[str, Any]  # Use a flexible type for the complex nested structure
