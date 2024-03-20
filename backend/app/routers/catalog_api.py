"""
This module defines the API routing for the catalog endpoints of a scholarly communication platform using FastAPI.
It provides routes to search for academic papers, authors, topics, and citation relationships based on a variety of
filters, allowing users to retrieve detailed information and establish connections between different entities within
the academic landscape. The endpoints return structured responses suitable for constructing search results and
citation trees, as well as for exploring co-authorship and topic-related articles.
"""

from fastapi import APIRouter, Depends

from ..services.catalog import search_papers_by_filter_as_response, search_topics_by_filter_as_response, \
    search_authors_by_filter_as_response, search_same_topic_by_filter_as_response, \
    search_co_author_by_filter_as_response, search_cited_tree_by_filter_as_response
from ..services.models import ArticleFilter, TopicFilter, AuthorFilter
from ..services.schema import PaperResponse, TopicResponse, SameTopicResponseSchema, CoAuthorResponseSchema, \
    CitedTreeResponseSchema, AuthorResponse
from .response_example import search_papers_example, search_topics_example, search_authors_example, \
    same_topic_example, co_author_example, cited_tree_example

# Initialize the API router
router = APIRouter(
    prefix="/catalog",
    tags=["catalog"],
    responses={404: {"description": "Not found"}},
)


@router.get("/",
            summary="Catalog API Root",
            description="This is the root endpoint of the Catalog API. It provides a quick check to ensure the API is "
                        "operational and to discover the base URI.",
            response_description="Provides the root URI for the Catalog API.",
            responses={
                200: {
                    "description": "Successful Response",
                    "content": {
                        "application/json": {
                            "example": {"uri": "/catalog"}
                        }
                    },
                },
                500: {
                    "description": "Internal Server Error",
                    "content": {
                        "application/json": {
                            "example": {"detail": "Internal server error"}
                        }
                    },
                },
            })
async def root():
    """
    The root endpoint of the Catalog API.

    This endpoint returns a simple JSON response indicating the base URI for the Catalog routes.
    """
    return {"uri": "/catalog"}


@router.get("/papers/search",
            response_model=PaperResponse,
            summary="Search for Papers",
            description="Search for papers based on various filters like title, publication date, DOI, and more.",
            response_description="A list of papers matching the search criteria.",
            responses={
                200: {
                    "description": "Papers found based on the search criteria",
                    "content": {
                        "application/json": {
                            "example": search_papers_example
                        }
                    },
                },
                500: {
                    "description": "Internal Server Error",
                    "content": {
                        "application/json": {
                            "example": {
                                "code": 500,
                                "msg": "Internal Server Error",
                                "data": None
                            }
                        }
                    }
                }
            }
            )
async def search_papers(article_filter: ArticleFilter = Depends(ArticleFilter)):
    """
    Search papers by filter.

    - **title**: Filter papers by title.
    - **abstract**: Search by keyword in the paper abstract.
    - **publisher**: Filter papers by the publisher's name.
    - **date**: Filter papers published on a specific date or within a date range.
      The date format should be 'YYYY-MM-DD', 'YYYY-MM', or 'YYYY'.
    - **issn**: Filter papers by the International Standard Serial Number.
    - **eissn**: Filter papers by the Electronic International Standard Serial Number.
    - **volume**: Filter papers by the volume in which they were published.
    - **issue**: Filter papers by the issue in which they were published.
    - **page**: Filter papers by the page number on which they appear.
    - **doi**: Filter papers by the Digital Object Identifier.
    - **meeting**: Filter papers presented at a specific meeting or conference.
    - **file_path**: Filter papers by the file path of the document.
    - **type**: Filter papers by the type of document (e.g., article, review).
    - **container_title**: Filter papers by the title of the container (e.g., journal, conference proceedings)
    in which they are published.

    The endpoint returns a list of papers that match the provided filters.

    ### Example request
    `GET /catalog/papers/search?title=mpi`
    """
    return search_papers_by_filter_as_response(article_filter)


@router.get("/topics/search",
            response_model=TopicResponse,
            summary="Search for Topics",
            description="Search for topics based on topic ID or name.",
            response_description="A list of topics matching the search criteria.",
            responses={
                200: {
                    "description": "Topics found based on the search criteria",
                    "content": {
                        "application/json": {
                            "example": search_topics_example
                        }
                    },
                },
                500: {
                    "description": "Internal Server Error",
                    "content": {
                        "application/json": {
                            "example": {
                                "code": 500,
                                "msg": "Internal Server Error",
                                "data": None
                            }
                        }
                    }
                }
            })
async def search_topics(topic_filter: TopicFilter = Depends()):
    """
    Search topics by filter.

    - **topic_id**: Filter topics by topic ID.
    - **name**: Filter topics by name.

    The endpoint returns a list of topics that match the provided filters.
    Filtering by topic ID can be particularly useful for retrieving a specific topic directly,
    while filtering by name allows for broader searches based on topic titles or keywords within the titles.

    ### Example request
    `GET /catalog/topics/search?topic_id=22`
    """
    return search_topics_by_filter_as_response(topic_filter)


@router.get("/authors/search",
            response_model=AuthorResponse,
            summary="Search for Authors",
            description="Search for authors based on various filters like author ID, name, email, or affiliation.",
            response_description="A list of authors matching the search criteria.",
            responses={
                200: {
                    "description": "Authors found based on the search criteria",
                    "content": {
                        "application/json": {
                            "example": search_authors_example
                        }
                    },
                },
                500: {
                    "description": "Internal Server Error",
                    "content": {
                        "application/json": {
                            "example": {
                                "code": 500,
                                "msg": "Internal Server Error",
                                "data": None
                            }
                        }
                    }
                }
            })
async def search_authors(author_filter: AuthorFilter = Depends(AuthorFilter)):
    """
    Search authors by filter.

    - **author_id**: Filter authors by their unique identifier.
    - **name**: Filter authors by their name. This can include partial or full names.
    - **email**: Filter authors by their email address.
    This can be useful for identifying authors with specific institutional or personal email domains.
    - **affiliation**: Filter authors by their affiliation with institutions or organizations.
    This can help identify authors associated with specific universities, research centers, or companies.

    The endpoint returns a list of authors that match the provided filters. This functionality is especially useful for
    disambiguating authors with common names by using additional filters like email or affiliation.

    ### Example request
    `GET /catalog/authors/search?name=tom`
    """
    return search_authors_by_filter_as_response(author_filter)


# Future work
# @router.get("/topic-connection", response_model=TopicConnectionResponseSchema)
# async def get_topic_connection():
#     authors = [AuthorSchema(id=i, name=f"author {i}",
#                             email=f"{i}@test.com", affiliation=f"affiliation {i}") for i in range(1, 6)]
#     original_topic = {"id": 1, "name": "searched origin topic", "papers": [1, 2, 3, 4, 5, 6]}
#     topics = [
#         {"id": i, "name": f"topic {i}", "original": i == 1}
#         for i in range(1, 8)
#     ]
#     connections = [
#         {"topic": i, "papers": [j for j in range(1, i + 7)]}
#         for i in range(1, 8)
#     ]
#     papers = [
#         {"id": i, "title": f"title {i}", "authors": authors}
#         for i in range(1, 19)
#     ]
#
#     return TopicConnectionResponseSchema(code=200, msg="success",
#                                          data={"original": original_topic,
#                                                "topics": topics,
#                                                "connections": connections,
#                                                "papers": papers})


@router.get("/same-topic",
            response_model=SameTopicResponseSchema,
            summary="Articles under the Same Topic",
            description="Retrieve articles that are related to the same topic based on a comprehensive set of article "
                        "filters.",
            response_description="A structure containing topics and their related articles.",
            responses={
                200: {
                    "description": "Articles found based on the search criteria",
                    "content": {
                        "application/json": {
                            "example": same_topic_example
                        }
                    }
                },
                500: {
                    "description": "Internal Server Error",
                    "content": {
                        "application/json": {
                            "example": {
                                "code": 500,
                                "msg": "Internal Server Error",
                                "data": None
                            }
                        }
                    }
                }
            })
async def get_same_topic(article_filter: ArticleFilter = Depends(ArticleFilter)):
    """
    Retrieve articles related to the same topic based on the article filter.

    The available filters include:
    - **article_id**: Filter articles by their unique identifier.
    - **title**: Filter articles by title. Useful for finding articles related to a specific subject matter.
    - **abstract**: Filter by keywords or phrases in the abstract to find articles on similar topics.
    - **publisher**: Filter articles published by a specific publisher.
    - **date**: Filter articles published on a specific date or within a date range.
    Formats include 'YYYY-MM-DD', 'YYYY-MM', or 'YYYY'.
    - **issn**, **eissn**: Filter articles by their ISSN or EISSN numbers,
    useful for targeting publications within specific journals.
    - **volume**, **issue**, **page**: Filter articles that appear in a specific volume, issue, or page number.
    - **doi**: Use the Digital Object Identifier to filter for specific articles.
    - **meeting**: Find articles presented at specific conferences or meetings.
    - **file_path**: Filter articles based on the file path of the document,
    useful for internal document management systems.
    - **type**: Filter by the type of document, such as 'research article', 'review', etc.
    - **container_title**: Filter articles within a specific journal or conference proceedings by the container's title.

    This endpoint returns a structured response containing topics and their related articles, based on the
    comprehensive filters applied to an initial article. This enables users to explore the landscape of related
    research on specific topics.

    ### Example request
    `GET /catalog/same-topic?article_id=98`
    """
    return search_same_topic_by_filter_as_response(article_filter)


@router.get("/co-author",
            response_model=CoAuthorResponseSchema,
            summary="Co-authorship Information",
            description="Retrieve co-authorship information based on an article's filter.",
            response_description="A structure containing authors and their co-authored articles.",
            responses={
                200: {
                    "description": "Co-authorship information found based on the search criteria",
                    "content": {
                        "application/json": {
                            "example": co_author_example
                        }
                    }
                },
                500: {
                    "description": "Internal Server Error",
                    "content": {
                        "application/json": {
                            "example": {
                                "code": 500,
                                "msg": "Internal Server Error",
                                "data": None
                            }
                        }
                    }
                }
            })
async def get_co_author_by_filter(article_filter: ArticleFilter = Depends(ArticleFilter)):
    """
    Get co-authorship information based on the article filter.

    The available filters include:
    - **article_id**: Filter articles by their unique identifier.
    - **title**: Filter articles by title. Useful for finding articles related to a specific subject matter.
    - **abstract**: Filter by keywords or phrases in the abstract to find articles on similar topics.
    - **publisher**: Filter articles published by a specific publisher.
    - **date**: Filter articles published on a specific date or within a date range.
    Formats include 'YYYY-MM-DD', 'YYYY-MM', or 'YYYY'.
    - **issn**, **eissn**: Filter articles by their ISSN or EISSN numbers,
    useful for targeting publications within specific journals.
    - **volume**, **issue**, **page**: Filter articles that appear in a specific volume, issue, or page number.
    - **doi**: Use the Digital Object Identifier to filter for specific articles.
    - **meeting**: Find articles presented at specific conferences or meetings.
    - **file_path**: Filter articles based on the file path of the document,
    useful for internal document management systems.
    - **type**: Filter by the type of document, such as 'research article', 'review', etc.
    - **container_title**: Filter articles within a specific journal or conference proceedings by the container's title.

    The endpoint returns a structure containing authors and their co-authored articles,
    based on the filters applied to an initial article.

    ### Example request
    `GET /catalog/co-author?article_id=9`
    """
    return search_co_author_by_filter_as_response(article_filter)


@router.get("/cited-tree",
            response_model=CitedTreeResponseSchema,
            summary="Cited Tree of an Article",
            description="Retrieve the citation tree of an article based on an article's filter.",
            response_description="A structure containing the cited articles and their relationships.",
            responses={
                200: {
                    "description": "Cited tree found based on the search criteria",
                    "content": {
                        "application/json": {
                            "example": cited_tree_example
                        }
                    }
                },
                500: {
                    "description": "Internal Server Error",
                    "content": {
                        "application/json": {
                            "example": {
                                "code": 500,
                                "msg": "Internal Server Error",
                                "data": None
                            }
                        }
                    }
                }
            })
async def get_cited_tree_by_filter(article_filter: ArticleFilter = Depends(ArticleFilter)):
    """
    Get the citation tree of an article based on the article filter.

    The available filters include:
    - **article_id**: Filter articles by their unique identifier.
    - **title**: Filter articles by title. Useful for finding articles related to a specific subject matter.
    - **abstract**: Filter by keywords or phrases in the abstract to find articles on similar topics.
    - **publisher**: Filter articles published by a specific publisher.
    - **date**: Filter articles published on a specific date or within a date range.
    Formats include 'YYYY-MM-DD', 'YYYY-MM', or 'YYYY'.
    - **issn**, **eissn**: Filter articles by their ISSN or EISSN numbers,
    useful for targeting publications within specific journals.
    - **volume**, **issue**, **page**: Filter articles that appear in a specific volume, issue, or page number.
    - **doi**: Use the Digital Object Identifier to filter for specific articles.
    - **meeting**: Find articles presented at specific conferences or meetings.
    - **file_path**: Filter articles based on the file path of the document,
    useful for internal document management systems.
    - **type**: Filter by the type of document, such as 'research article', 'review', etc.
    - **container_title**: Filter articles within a specific journal or conference proceedings by the container's title.

    The endpoint returns a structure containing the cited articles and their relationships,
    based on the filters applied to an initial article.

    ### Example request
    `GET /catalog/cited-tree?article_id=98`
    """
    return search_cited_tree_by_filter_as_response(article_filter)
