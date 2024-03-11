from fastapi import APIRouter

# Initialize the API router
router = APIRouter(
    prefix="/catalog",
    tags=["catalog"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def root():
    return {"uri": "/catalog"}
