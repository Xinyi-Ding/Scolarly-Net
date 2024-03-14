from fastapi import APIRouter
from backend.app.services.schema import PaperResponse, TopicResponse, AuthorResponse

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
    sample_data = [
        {"id": i, "title": f"example paper title {i}", "authors": "author 1, author 2, author 3, author 4, author 5"}
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
