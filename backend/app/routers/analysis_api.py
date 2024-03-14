from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
from app.services import analysis
from datetime import date

from backend.app.services.schema import TopicConnectionResponseVO, SameTopicResponseVO, DashboardResponseVO, \
    DashboardItemVO, CoAuthorResponseVO, CitedConnectionItemVO, CitedPaperItemVO, CitedTreeResponseVO

# Initialize the API router with a prefix and tags
router = APIRouter(
    prefix="/analysis",
    tags=["analysis"],
    responses={404: {"description": "Not found"}},
)

papers_directory = Path('app') / 'data' / 'Papers'
papers_directory.mkdir(parents=True, exist_ok=True)

@router.get("/")
async def root():
    return {'uri': '/analysis'}


@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    try:
        file_location = papers_directory / Path(file.filename)
        with open(file_location, "wb+") as file_object:
            content = await file.read()
            file_object.write(content)
        await file.close()
        article = analysis.get_artical(analysis.get_extracted_xml(str(file_location), grobid_server="http://localhost:8070"))
        res = {"code": 200, "message": "File uploaded successfully", "data": article.to_json()}
        return JSONResponse(status_code=200, content=res)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Could not save file")

@router.get("/topic-connection", response_model=TopicConnectionResponseVO)
async def get_topic_connection():
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
        {"id": i, "title": f"title {i}", "authors": "author 1, author 2, author 3, author 4, author 5"}
        for i in range(1, 19)
    ]

    return TopicConnectionResponseVO(code=200, msg="success",
                                     data={"original": original_topic, "topics": topics, "connections": connections,
                                           "papers": papers})


@router.get("/same-topic", response_model=SameTopicResponseVO)
async def get_same_topic():
    original_paper = {"id": 1, "title": "searched origin paper title", "authors": "author 1, author 2, author 3, "
                                                                                  "author 4, author 5"}
    topics = [{"id": i, "name": f"topic {i}"} for i in range(1, 5)]
    connections = [{"topic": i, "papers": [j for j in range(1, i + 5)]} for i in range(1, 5)]
    papers = [
        {"id": i, "title": f"title {i}", "authors": "author 1, author 2, author 3, author 4, author 5",
         "original": i == 1}
        for i in range(1, 19)
    ]

    return SameTopicResponseVO(code=200, msg="success", data={"original": original_paper, "topics": topics,
                                                              "connections": connections, "papers": papers})


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
    original_author = {"id": 1,
                       "name": "author 1",
                       "original": True
                       }
    authors = [
        {"id": i, "name": f"author {i}", "original": i == 1}
        for i in range(1, 9)
    ]
    papers = [
        {"id": i, "title": f"title {i}", "authors": ", ".join([f"author {j}" for j in range(1, min(i + 1, 6))])}
        for i in range(1, 19)
    ]
    connections = [
        {"author": i, "papers": [j for j in range(1, min(i + 10, 19))]}
        for i in range(1, 9)
    ]

    return CoAuthorResponseVO(code=200, msg="success", data={"original": original_author, "authors": authors,
                                                             "papers": papers, "connections": connections})


@router.get("/cited-tree", response_model=CitedTreeResponseVO)
async def get_cited_tree(paper_id: int = 1):
    # Example cited tree data, replace with actual data retrieval as needed
    original_paper = CitedPaperItemVO(
        id=1,
        title="searched origin paper title",
        authors="author 1, author 2, author 3, author 4, author 5",
        original=True
    )
    papers = [original_paper] + [
        CitedPaperItemVO(
            id=i,
            title=f"title {i}",
            authors="author 1, author 2, author 3, author 4, author 5",
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
                               data={"original": original_paper, "connections": connections, "papers": papers})
