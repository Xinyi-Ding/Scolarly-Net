from fastapi import APIRouter, Depends

from backend.app.services.catalog import search_papers_by_filter_as_response, search_topics_by_filter_as_response, \
    search_authors_by_filter_as_response, search_same_topic_by_filter_as_response, \
    search_co_author_by_filter_as_response, search_cited_tree_by_filter_as_response
from backend.app.services.models import ArticleFilter, TopicFilter, AuthorFilter
from backend.app.services.schema import PaperResponse, TopicResponse, SameTopicResponseSchema, CoAuthorResponseSchema, \
    CitedTreeResponseSchema, AuthorResponse

# Initialize the API router
router = APIRouter(
    prefix="/catalog",
    tags=["catalog"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def root():
    return {"uri": "/catalog"}


@router.get("/papers/search", response_model=PaperResponse)
async def search_papers(article_filter: ArticleFilter = Depends(ArticleFilter)):
    """
    Search papers by filter
    :param article_filter: The filter of the article
    :return: The response of the papers
    """
    return search_papers_by_filter_as_response(article_filter)


@router.get("/topics/search", response_model=TopicResponse)
async def search_topics(topic_filter: TopicFilter = Depends(TopicFilter)):
    """
    Search topics by filter
    :param topic_filter: The filter of the topic
    :return: The response of the topics
    """
    return search_topics_by_filter_as_response(topic_filter)


@router.get("/authors/search", response_model=AuthorResponse)
async def search_authors(author_filter: AuthorFilter = Depends(AuthorFilter)):
    """
    Search authors by filter
    :param author_filter: The filter of the author
    :return: The response of the authors
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


@router.get("/same-topic", response_model=SameTopicResponseSchema)
async def get_same_topic(article_filter: ArticleFilter = Depends(ArticleFilter)):
    """
    Get the same topic of the article
    :param article_filter: The filter of the article
    :return: The response of the same topic
    """
    return search_same_topic_by_filter_as_response(article_filter)


@router.get("/co-author", response_model=CoAuthorResponseSchema)
async def get_co_author(article_filter: ArticleFilter = Depends(ArticleFilter)):
    """
    Get the co-author of the article
    :param article_filter: The filter of the article
    :return: The response of the co-author
    """
    return search_co_author_by_filter_as_response(article_filter)


@router.get("/cited-tree", response_model=CitedTreeResponseSchema)
async def get_cited_tree(article_filter: ArticleFilter = Depends(ArticleFilter)):
    """
    Get the cited tree of the article
    :param article_filter: The filter of the article
    :return: The response of the cited tree
    """
    return search_cited_tree_by_filter_as_response(article_filter)
