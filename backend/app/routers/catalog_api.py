from fastapi import APIRouter, Depends

from ..services.catalog import search_papers_by_filter_as_response, search_topics_by_filter_as_response, \
    search_authors_by_filter_as_response, search_same_topic_by_filter_as_response, \
    search_co_author_by_filter_as_response, search_cited_tree_by_filter_as_response
from ..services.models import ArticleFilter, TopicFilter, AuthorFilter
from ..services.schema import PaperResponse, TopicResponse, SameTopicResponseSchema, CoAuthorResponseSchema, \
    CitedTreeResponseSchema, AuthorResponse

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
            response_description="Provides a welcome message along with the root URI for the Catalog API.")
async def root():
    """
    The root endpoint of the Catalog API.

    This endpoint returns a simple JSON response indicating the base URI for the Catalog routes and a welcoming message.
    """
    return {'uri': '/catalog'}


@router.get("/papers/search",
            response_model=PaperResponse,
            summary="Search for Papers",
            description="Search for papers based on various filters like title, publication date, DOI, and more.",
            response_description="A list of papers matching the search criteria.")
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
    `GET /catalog/papers/search?article_id=98`
    ### Response
    {
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
              "email": null,
              "affiliation": "Brazilian National Institute for Space Research (INPE)"
            }
          ]
        }
      ]
    }
    """
    return search_papers_by_filter_as_response(article_filter)


@router.get("/topics/search",
            response_model=TopicResponse,
            summary="Search for Topics",
            description="Search for topics based on topic ID or name.",
            response_description="A list of topics matching the search criteria.")
async def search_topics(topic_filter: TopicFilter = Depends(TopicFilter)):
    """
    Search topics by filter.

    - **topic_id**: Filter topics by topic ID.
    - **name**: Filter topics by name.

    The endpoint returns a list of topics that match the provided filters.
    Filtering by topic ID can be particularly useful for retrieving a specific topic directly,
    while filtering by name allows for broader searches based on topic titles or keywords within the titles.

    ### Example request
    `GET /catalog/topics/search?topic_id=98`
    ### Response
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
    """
    return search_topics_by_filter_as_response(topic_filter)


@router.get("/authors/search",
            response_model=AuthorResponse,
            summary="Search for Authors",
            description="Search for authors based on various filters like author ID, name, email, or affiliation.",
            response_description="A list of authors matching the search criteria.")
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
    `GET /catalog/authors/search?name=Jack`
    ### Response
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
            response_description="A structure containing topics and their related articles.")
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
    ### Response
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
                "email": null,
                "affiliation": "Brazilian National Institute for Space Research (INPE)"
              }
            ]
          }
        ]
      }
    }
    """
    return search_same_topic_by_filter_as_response(article_filter)


@router.get("/co-author",
            response_model=CoAuthorResponseSchema,
            summary="Co-authorship Information",
            description="Retrieve co-authorship information based on an article's filter.",
            response_description="A structure containing authors and their co-authored articles.")
async def get_co_author(article_filter: ArticleFilter = Depends(ArticleFilter)):
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
    `GET /catalog/co-author?article_id=98`
    ### Response
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
            "email": null,
            "affiliation": "Brazilian National Institute for Space Research (INPE)"
          }
        ],
        "papers": [
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
                "email": null,
                "affiliation": "Brazilian National Institute for Space Research (INPE)"
              }
            ]
          }
        ]
      }
    }
    """
    return search_co_author_by_filter_as_response(article_filter)


@router.get("/cited-tree",
            response_model=CitedTreeResponseSchema,
            summary="Cited Tree of an Article",
            description="Retrieve the citation tree of an article based on an article's filter.",
            response_description="A structure containing the cited articles and their relationships.")
async def get_cited_tree(article_filter: ArticleFilter = Depends(ArticleFilter)):
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
    ### Response
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
                "email": null,
                "affiliation": null
              },
              {
                "id": 169,
                "name": "R. Mesiar",
                "email": null,
                "affiliation": null
              },
              {
                "id": 188,
                "name": "D. Gómez",
                "email": null,
                "affiliation": null
              },
              {
                "id": 189,
                "name": "J. Yáñez",
                "email": null,
                "affiliation": null
              },
              {
                "id": 229,
                "name": "B. Baets",
                "email": null,
                "affiliation": null
              },
              {
                "id": 230,
                "name": "T.-partitions",
                "email": null,
                "affiliation": null
              }
            ]
          },
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
                "email": null,
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
                "email": null,
                "affiliation": null
              },
              {
                "id": 222,
                "name": "F. Esteva",
                "email": null,
                "affiliation": null
              },
              {
                "id": 223,
                "name": "L. Godo",
                "email": null,
                "affiliation": null
              },
              {
                "id": 224,
                "name": "V. Torra",
                "email": null,
                "affiliation": null
              }
            ]
          }
        ]
      }
    }
    """
    return search_cited_tree_by_filter_as_response(article_filter)
