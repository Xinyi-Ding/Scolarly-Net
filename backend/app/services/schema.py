# Pydantic model for the Response
from typing import Any, Optional
from datetime import date

from pydantic import BaseModel


class ResponseSchema(BaseModel):
    code: int = 200
    msg: str = "success"  # By default, the response is successful (But in practice, it should be "error" if failed)
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

    class Config:
        schema_extra = {
            "example": {
                "code": 200,
                "msg": "Success",
                "data": [
                    {
                        "id": 98,
                        "title": "A method for deriving order compatible fuzzy relations from convex fuzzy partitions",
                        "authors": [
                            {
                                "id": 219,
                                "name": "Sandra Sandri",
                                "email": "sandra.sandri@inpe.br",
                                "affiliation": "Brazilian National Institute for Space Research (INPE)"
                            },
                            {
                                "id": 220,
                                "name": "Flávia Toledo Martins-Bedê",
                                "email": None,
                                "affiliation": "Brazilian National Institute for Space Research (INPE)"
                            }
                        ]
                    }
                ]
            }
        }


class TopicItemSchema(BaseModel):
    id: int = None
    topic: str = None
    count: int = None


class TopicResponse(ResponseSchema):
    data: list[TopicItemSchema] = []

    class Config:
        schema_extra = {
            "example": [
                {
                    "code": 200,
                    "msg": "Success",
                    "data": [
                        {
                            "id": 98,
                            "topic": "Network data models",
                            "count": 1
                        }
                    ]
                }
            ]
        }


class AuthorItemSchema(BaseModel):
    id: int = None
    name: str = None
    count: int = None


class AuthorResponse(ResponseSchema):
    data: list[AuthorItemSchema] = []

    class Config:
        schema_extra = {
            "example": [
                {
                    "code": 200,
                    "msg": "Success",
                    "data": [
                        {
                            "id": 2093,
                            "name": "Brendon Jackson",
                            "count": 1
                        },
                        {
                            "id": 2279,
                            "name": "Bryan L. Jackson",
                            "count": 1
                        },
                        {
                            "id": 5004,
                            "name": "Jack Brown",
                            "count": 1
                        },
                        {
                            "id": 1194,
                            "name": "Jack Dongarra",
                            "count": 2
                        },
                        {
                            "id": 4987,
                            "name": "Jack Hidary",
                            "count": 1
                        },
                        {
                            "id": 1848,
                            "name": "Jack J. Dongarra",
                            "count": 1
                        },
                        {
                            "id": 3387,
                            "name": "Jeff Jackson",
                            "count": 1
                        },
                        {
                            "id": 4409,
                            "name": "Kenneth R. Jackson",
                            "count": 1
                        }
                    ]
                }
            ]
        }


class SameTopicConnectionItemSchema(BaseModel):
    topic: int = None
    papers: list[int] = []


class SameTopicDataSchema(BaseModel):
    connections: list[SameTopicConnectionItemSchema] = []
    topics: list[TopicSchema] = []
    papers: list[PaperItemSchema] = []


class SameTopicResponseSchema(ResponseSchema):
    data: SameTopicDataSchema = {}

    class Config:
        schema_extra = {
            "example": [
                {
                    "code": 200,
                    "msg": "Success",
                    "data": {
                        "connections": [
                            {
                                "topic": 10,
                                "papers": [
                                    98
                                ]
                            },
                            {
                                "topic": 11,
                                "papers": [
                                    98
                                ]
                            },
                            {
                                "topic": 12,
                                "papers": [
                                    98
                                ]
                            },
                            {
                                "topic": 13,
                                "papers": [
                                    98
                                ]
                            },
                            {
                                "topic": 14,
                                "papers": [
                                    98
                                ]
                            }
                        ],
                        "topics": [
                            {
                                "id": 10,
                                "name": "Similarity relations"
                            },
                            {
                                "id": 11,
                                "name": "Fuzzy relations"
                            },
                            {
                                "id": 12,
                                "name": "Fuzzy partitions"
                            },
                            {
                                "id": 13,
                                "name": "Total order"
                            },
                            {
                                "id": 14,
                                "name": "T-indistinguishable operators"
                            }
                        ],
                        "papers": [
                            {
                                "id": 98,
                                "title": "A method for deriving order compatible fuzzy relations from convex fuzzy "
                                         "partitions",
                                "authors": [
                                    {
                                        "id": 219,
                                        "name": "Sandra Sandri",
                                        "email": "sandra.sandri@inpe.br",
                                        "affiliation": "Brazilian National Institute for Space Research (INPE)"
                                    },
                                    {
                                        "id": 220,
                                        "name": "Flávia Toledo Martins-Bedê",
                                        "email": None,
                                        "affiliation": "Brazilian National Institute for Space Research (INPE)"
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }


class CoAuthorConnectionItemSchema(BaseModel):
    author: int = None
    papers: list[int] = []


class CoAuthorDataSchema(BaseModel):
    connections: list[CoAuthorConnectionItemSchema] = []
    authors: list[AuthorSchema] = []
    papers: list[PaperItemSchema] = []


class CoAuthorResponseSchema(ResponseSchema):
    data: CoAuthorDataSchema = {}

    class Config:
        schema_extra = {
            "example": [
                {
                    "code": 200,
                    "msg": "Success",
                    "data": {
                        "connections": [
                            {
                                "author": 219,
                                "papers": [
                                    98
                                ]
                            },
                            {
                                "author": 220,
                                "papers": [
                                    98
                                ]
                            }
                        ],
                        "authors": [
                            {
                                "id": 219,
                                "name": "Sandra Sandri",
                                "email": "sandra.sandri@inpe.br",
                                "affiliation": "Brazilian National Institute for Space Research (INPE)"
                            },
                            {
                                "id": 220,
                                "name": "Flávia Toledo Martins-Bedê",
                                "email": None,
                                "affiliation": "Brazilian National Institute for Space Research (INPE)"
                            }
                        ],
                        "papers": [
                            {
                                "id": 98,
                                "title": "A method for deriving order compatible fuzzy relations from convex fuzzy "
                                         "partitions",
                                "authors": [
                                    {
                                        "id": 219,
                                        "name": "Sandra Sandri",
                                        "email": "sandra.sandri@inpe.br",
                                        "affiliation": "Brazilian National Institute for Space Research (INPE)"
                                    },
                                    {
                                        "id": 220,
                                        "name": "Flávia Toledo Martins-Bedê",
                                        "email": None,
                                        "affiliation": "Brazilian National Institute for Space Research (INPE)"
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }


class DashboardItemSchema(BaseModel):
    id: int = None
    title: str = None
    authors: list[str] = []
    affiliations: list[str] = []
    date: date = None
    doi: str = None
    keywords: list[str] = []
    references: int = None


# class DashboardResponseSchema(ResponseSchema):
#     data: DashboardItemSchema = None


class CitedConnectionItemSchema(BaseModel):
    from_paper: int
    to_paper: list[int]


class CitedTreeDataSchema(BaseModel):
    connections: list[CitedConnectionItemSchema]
    papers: list[PaperItemSchema]


class CitedTreeResponseSchema(ResponseSchema):
    data: CitedTreeDataSchema = {}

    class Config:
        schema_extra = {
            "example": [
                {
                    "code": 200,
                    "msg": "Success",
                    "data": {
                        "connections": [
                            {
                                "from_paper": 98,
                                "to_paper": [
                                    75,
                                    99,
                                ]
                            }
                        ],
                        "papers": [
                            {
                                "id": 75,
                                "title": "A coloring algorithm for image classification, Inf",
                                "authors": [
                                    {
                                        "id": 142,
                                        "name": "J. Montero",
                                        "email": None,
                                        "affiliation": None
                                    },
                                    {
                                        "id": 169,
                                        "name": "R. Mesiar",
                                        "email": None,
                                        "affiliation": None
                                    },
                                    {
                                        "id": 188,
                                        "name": "D. Gómez",
                                        "email": None,
                                        "affiliation": None
                                    },
                                    {
                                        "id": 189,
                                        "name": "J. Yáñez",
                                        "email": None,
                                        "affiliation": None
                                    },
                                    {
                                        "id": 229,
                                        "name": "B. Baets",
                                        "email": None,
                                        "affiliation": None
                                    },
                                    {
                                        "id": 230,
                                        "name": "T.-partitions",
                                        "email": None,
                                        "affiliation": None
                                    }
                                ]
                            },
                            {
                                "id": 98,
                                "title": "A method for deriving order compatible fuzzy relations from convex fuzzy "
                                         "partitions",
                                "authors": [
                                    {
                                        "id": 219,
                                        "name": "Sandra Sandri",
                                        "email": "sandra.sandri@inpe.br",
                                        "affiliation": "Brazilian National Institute for Space Research (INPE)"
                                    },
                                    {
                                        "id": 220,
                                        "name": "Flávia Toledo Martins-Bedê",
                                        "email": None,
                                        "affiliation": "Brazilian National Institute for Space Research (INPE)"
                                    }
                                ]
                            },
                            {
                                "id": 99,
                                "title": "On learning similarity relations in fuzzy case-based reasoning",
                                "authors": [
                                    {
                                        "id": 221,
                                        "name": "E. Armengol",
                                        "email": None,
                                        "affiliation": None
                                    },
                                    {
                                        "id": 222,
                                        "name": "F. Esteva",
                                        "email": None,
                                        "affiliation": None
                                    },
                                    {
                                        "id": 223,
                                        "name": "L. Godo",
                                        "email": None,
                                        "affiliation": None
                                    },
                                    {
                                        "id": 224,
                                        "name": "V. Torra",
                                        "email": None,
                                        "affiliation": None
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }
