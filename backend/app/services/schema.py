"""
This module defines a suite of Pydantic models for a scholarly communication API, handling the structure of
responses, and describing entities such as papers, authors, and topics. It includes schemas for individual items and
their collections, response structures, and specialized data formats for representing relationships such as
co-authorship and citation networks, catering to various endpoints of the API that serve an academic dashboard.
"""

from typing import Any, Optional
from pydantic import BaseModel, Field


class ResponseSchema(BaseModel):
    code: int = Field(200, title="HTTP status code", description="The HTTP status code of the response.")
    # By default, the response is successful (But in practice, it should be "error" if failed)
    msg: str = Field("success", title="Message", description="The message of the response.")
    data: list | dict | Any = Field(None, title="Data", description="The data of the response.")


class AuthorSchema(BaseModel):
    id: int = Field(None, title="Author ID", description="The unique identifier of the author.")
    name: str = Field(None, title="Author Name", description="The name of the author.")
    email: str = Field(None, title="Author Email", description="The email of the author.")
    affiliation: Optional[str] = Field(None, title="Author Affiliation", description="The affiliation of the author.")


class TopicSchema(BaseModel):
    id: int = Field(None, title="Topic ID", description="The unique identifier of the topic.")
    name: str = Field(None, title="Topic Name", description="The name of the topic.")
    # original: Optional[bool] = False


class PaperItemSchema(BaseModel):
    id: int = Field(None, title="Paper ID", description="The unique identifier of the paper.")
    title: str = Field(None, title="Paper Title", description="The title of the paper.")
    authors: list[AuthorSchema] = Field([], title="Paper Authors", description="The authors of the paper.")


class PaperResponse(ResponseSchema):
    data: list[PaperItemSchema] = Field([], title="Paper List", description="The list of papers.")


class TopicItemSchema(BaseModel):
    id: int = Field(None, title="Topic ID", description="The unique identifier of the topic.")
    topic: str = Field(None, title="Topic Name", description="The name of the topic.")
    count: int = Field(None, title="Paper Count", description="The number of papers in the topic.")


class TopicResponse(ResponseSchema):
    data: list[TopicItemSchema] = Field([], title="Topic List", description="The list of topics.")


class AuthorItemSchema(BaseModel):
    id: int = Field(None, title="Author ID", description="The unique identifier of the author.")
    name: str = Field(None, title="Author Name", description="The name of the author.")
    count: int = Field(None, title="Paper Count", description="The number of papers by the author.")


class AuthorResponse(ResponseSchema):
    data: list[AuthorItemSchema] = Field([], title="Author List", description="The list of authors.")


class SameTopicConnectionItemSchema(BaseModel):
    topic: int = Field(None, title="Topic ID", description="The unique identifier of the topic.")
    papers: list[int] = Field([], title="Paper List", description="The list of papers in the topic.")


class SameTopicDataSchema(BaseModel):
    connections: list[SameTopicConnectionItemSchema] = Field([],
                                                             title="Connection List",
                                                             description="The list of connections.")
    topics: list[TopicSchema] = Field([], title="Topic List", description="The list of topics.")
    papers: list[PaperItemSchema] = Field([], title="Paper List", description="The list of papers.")


class SameTopicResponseSchema(ResponseSchema):
    data: SameTopicDataSchema = Field({}, title="Data", description="The data of the response.")


class CoAuthorConnectionItemSchema(BaseModel):
    author: int = Field(None, title="Author ID", description="The unique identifier of the author.")
    papers: list[int] = Field([], title="Paper List", description="The list of papers by the author.")


class CoAuthorDataSchema(BaseModel):
    connections: list[CoAuthorConnectionItemSchema] = Field([],
                                                            title="Connection List",
                                                            description="The list of connections.")
    authors: list[AuthorSchema] = Field([], title="Author List", description="The list of authors.")
    papers: list[PaperItemSchema] = Field([], title="Paper List", description="The list of papers.")


class CoAuthorResponseSchema(ResponseSchema):
    data: CoAuthorDataSchema = Field({}, title="Data", description="The data of the response.")


class CitedConnectionItemSchema(BaseModel):
    from_paper: int = Field(..., title="From Paper ID", description="The unique identifier of the paper.")
    to_paper: list[int] = Field([], title="To Paper List", description="The list of papers cited by the from paper.")


class CitedTreeDataSchema(BaseModel):
    connections: list[CitedConnectionItemSchema] = Field([],
                                                         title="Connection List",
                                                         description="The list of connections.")
    papers: list[PaperItemSchema] = Field([], title="Paper List", description="The list of papers.")


class CitedTreeResponseSchema(ResponseSchema):
    data: CitedTreeDataSchema = Field({}, title="Data", description="The data of the response.")
