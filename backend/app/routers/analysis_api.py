from fastapi import APIRouter

# Initialize the API router with a prefix and tags
router = APIRouter(
    prefix="/analysis",
    tags=["analysis"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def root():
    return {'uri': '/analysis'}
