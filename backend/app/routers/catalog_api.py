from datetime import date

from fastapi import APIRouter

from backend.app.services.schema import PaperResponse, TopicResponse, AuthorResponse, TopicConnectionResponseVO, \
    SameTopicResponseVO, DashboardResponseVO, \
    DashboardItemVO, CoAuthorResponseVO, CitedConnectionItemVO, CitedPaperItemVO, CitedTreeResponseVO, AuthorVO

# Initialize the API router
router = APIRouter(
    prefix="/catalog",
    tags=["catalog"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def root():
    return {"uri": "/catalog"}


@router.get("/papers", response_model=PaperResponse)
async def get_papers():
    # Sample data to return
    authors = [AuthorVO(id=i, name=f"author {i}",
                        email=f"{i}@test.com", affiliation=f"affiliation {i}") for i in range(1, 6)]
    sample_data = [
        {"id": i, "title": f"example paper title {i}", "authors": authors}
        for i in range(1, 14)
    ]
    return PaperResponse(code=200, msg="success", data=sample_data)


@router.get("/topics", response_model=TopicResponse)
async def get_topics():
    # Sample data to return
    sample_data = [
        {"id": i, "topic": f"example topic {i}", "count": 100 + i * 100}
        for i in range(1, 21)
    ]
    return TopicResponse(code=200, msg="success", data=sample_data)


@router.get("/authors", response_model=AuthorResponse)
async def get_authors():
    # Sample data to return
    sample_data = [
        {"id": i, "name": f"author {i}", "count": 100 + i * 35}
        for i in range(1, 21)
    ]
    return AuthorResponse(code=200, msg="success", data=sample_data)


@router.get("/topic-connection", response_model=TopicConnectionResponseVO)
async def get_topic_connection():
    authors = [AuthorVO(id=i, name=f"author {i}",
                        email=f"{i}@test.com", affiliation=f"affiliation {i}") for i in range(1, 6)]
    original_topic = {"id": 1, "name": "searched origin topic", "papers": [1, 2, 3, 4, 5, 6]}
    topics = [
        {"id": i, "name": f"topic {i}", "original": i == 1}
        for i in range(1, 8)
    ]
    connections = [
        {"topic": i, "papers": [j for j in range(1, i + 7)]}
        for i in range(1, 8)
    ]
    papers = [
        {"id": i, "title": f"title {i}", "authors": authors}
        for i in range(1, 19)
    ]

    return TopicConnectionResponseVO(code=200, msg="success",
                                     data={"original": original_topic, "topics": topics, "connections": connections,
                                           "papers": papers})


@router.get("/same-topic", response_model=SameTopicResponseVO)
async def get_same_topic():
    authors = [AuthorVO(id=i, name=f"author {i}",
                        email=f"{i}@test.com", affiliation=f"affiliation {i}") for i in range(1, 6)]
    original_paper = {"id": 1, "title": "searched origin paper title", "authors": authors, "original": True}
    topics = [{"id": i, "name": f"topic {i}"} for i in range(1, 5)]
    connections = [{"topic": i, "papers": [j for j in range(1, i + 5)]} for i in range(1, 5)]
    papers = [
        {"id": i, "title": f"title {i}", "authors": "author 1, author 2, author 3, author 4, author 5",
         "original": i == 1}
        for i in range(1, 19)
    ]

    return SameTopicResponseVO(code=200, msg="success", data={"connections": connections,
                                                              "topics": topics,
                                                              "original": original_paper,
                                                              "papers": papers})


@router.get("/dashboard", response_model=DashboardResponseVO)
async def get_dashboard():
    dashboard_data = DashboardItemVO(
        id=4,
        title="In Situ Workflows at Exascale: System Software to the Rescue",
        authors=["Matthieu Dreher", "Swann Perarnau", "Tom Peterka", "Kamil Iskra", "Pete Beckman"],
        affiliations=[],
        date=date(2017, 11, 12),
        doi="10.1145/3144769.3144774",
        keywords=["Argo", "MPI", "In Situ Workflows", "Exascale", "System Software"],
        references=23
    )

    return DashboardResponseVO(code=200, msg="success", data=dashboard_data)


@router.get("/co-author", response_model=CoAuthorResponseVO)
async def get_co_author(author_id: int = 1):
    # Example co-author data, replace with actual data retrieval as needed
    original_author = {"id": 2,
                       "title": "searched origin author",
                       "authors": [
                           {
                               "id": 1,
                               "name": "author 1",
                               "email": "author1@test.test"
                           }]
                       }
    authors = [
        {"id": i, "name": f"author {i}"}
        for i in range(1, 9)
    ]
    authors_vo = [AuthorVO(id=i, name=f"author {i}",
                           email=f"{i}@test.com", affiliation=f"affiliation {i}") for i in range(1, 6)]
    papers = [
        {"id": i, "title": f"title {i}", "authors": authors_vo}
        for i in range(1, 19)
    ]
    connections = [
        {"author": i, "papers": [j for j in range(1, min(i + 10, 19))]}
        for i in range(1, 9)
    ]

    return CoAuthorResponseVO(code=200, msg="success", data={"connections": connections,
                                                             "authors": authors,
                                                             "original": original_author,
                                                             "papers": papers,
                                                             })


@router.get("/cited-tree", response_model=CitedTreeResponseVO)
async def get_cited_tree(paper_id: int = 1):
    # Example cited tree data, replace with actual data retrieval as needed
    authors = [AuthorVO(id=i, name=f"author {i}",
                        email=f"{i}@test.com", affiliation=f"affiliation {i}") for i in range(1, 6)]
    original_paper = CitedPaperItemVO(
        id=1,
        title="searched origin paper title",
        authors=authors,
        original=True
    )
    papers = [original_paper] + [
        CitedPaperItemVO(
            id=i,
            title=f"title {i}",
            authors=authors,
            original=False
        ) for i in range(2, 18)
    ]
    connections = [
        CitedConnectionItemVO(from_paper=1, to=[2, 3, 4, 5]),
        CitedConnectionItemVO(from_paper=2, to=[6, 7, 8]),
        CitedConnectionItemVO(from_paper=4, to=[9, 10]),
        CitedConnectionItemVO(from_paper=5, to=[11, 12, 13, 14]),
        CitedConnectionItemVO(from_paper=6, to=[15, 16]),
        CitedConnectionItemVO(from_paper=8, to=[17])
    ]

    return CitedTreeResponseVO(code=200, msg="success",
                               data={"connections": connections,
                                     "original": original_paper,
                                     "papers": papers})
