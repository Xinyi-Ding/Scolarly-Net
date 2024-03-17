from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
from ..services import analysis


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
        article = analysis.get_artical(
            analysis.get_extracted_xml(str(file_location), grobid_server="http://localhost:8070"))
        article.content.keywords = analysis.get_topics_from_article(article)
        res = {"code": 200, "message": "File uploaded successfully", "data": article.to_json()}
        return JSONResponse(status_code=200, content=res)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Could not save file")
