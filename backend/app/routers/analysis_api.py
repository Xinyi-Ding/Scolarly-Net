from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
from ..services import analysis
from ..services.catalog import save_parse_article
import os


# Initialize the API router with a prefix and tags
router = APIRouter(
    prefix="/analysis",
    tags=["analysis"],
    responses={404: {"description": "Not found"}},
)

papers_directory = Path().cwd() / "app" / "tmp" / "Papers"
xml_directory = Path().cwd() / "app" / "tmp" / "xml"
papers_directory.mkdir(parents=True, exist_ok=True)
xml_directory.mkdir(parents=True, exist_ok=True)


@router.get("/")
async def root():
    return {'uri': '/analysis'}


@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    print(Path().cwd())
    try:
        file_location = papers_directory / Path(file.filename)
        print("File received")
        with open(file_location, "wb+") as file_object:
            content = await file.read()
            file_object.write(content)
        await file.close()
        print("File saved to disk: ", file_location)
        xml_location = analysis.get_extracted_xml(str(file_location), grobid_server="http://localhost:8070")
        article = analysis.get_article_object(xml_location)
        print("Article object created")
        # articleVO = save_parse_article(article)
        print("Article saved to database")
        res = {"code": 200,
               "message": "File uploaded successfully",
               "data": article.to_json(article_id=122)
               }
        os.remove(file_location)
        os.remove(xml_location)
        print("tmp files removed")
        return JSONResponse(status_code=200, content=res)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Could not save file")
