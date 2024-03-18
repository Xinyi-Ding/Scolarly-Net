from fastapi import APIRouter, File, UploadFile, HTTPException
from pathlib import Path

from starlette.responses import JSONResponse

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


@router.get("/",
            summary="Analysis API Root",
            description="This is the root endpoint of the Analysis API. It can be used to check if the API is up and "
                        "running.",
            response_description="A welcome message and the root URI.")
async def root():
    """
    The root endpoint of the Analysis API.

    This endpoint provides a simple JSON response indicating the base URI for the analysis routes and a welcome message.
    """
    return {'uri': '/analysis'}


@router.post("/upload/",
             summary="Upload a document",
             description="Upload a document to the server and process it. The document will be saved, analyzed, "
                         "and the extracted information will be stored.",
             response_description="The response contains the status of the upload and any extracted information from"
                                  "the document.",
             responses={
                 200: {
                     "description": "Document uploaded and processed successfully.",
                     "content": {
                         "application/json": {
                             "example": {
                                 "code": 200,
                                 "message": "File uploaded successfully",
                                 "data": {
                                     "title": "Example Title",
                                     "authors": [{"name": "Author One", "affiliation": "University of Examples"}],
                                     "abstract": "This is an example of an abstract from the uploaded document.",
                                     "keywords": ["example", "document", "upload"]
                                 }
                             }
                         }
                     },
                 },
                 500: {
                     "description": "Internal Server Error",
                     "content": {
                         "application/json": {
                             "example": {"detail": "Could not save file"}
                         }
                     },
                 }
             })
async def upload_document(file: UploadFile = File(..., description="The document file to be uploaded.")):
    """
    Upload a document to the server and parse it.

    - **file**: The document file to be uploaded. The file will be processed to extract information.

    Upon successful upload, the document is saved to disk, and various processing tasks are performed on it,
    such as extracting text and analyzing content. The endpoint returns a JSON response containing the results
    of these operations.
    """
    """
    Upload a document to the server and parse it using GROBID
    :param file: The document to be uploaded
    :return: JSONResponse with the parsed document
    """
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
        article_vo = save_parse_article(article)
        print("Article saved to database")
        res = {"code": 200,
               "message": "File uploaded successfully",
               "data": article.to_json(article_id=article_vo.article_id)
               }
        os.remove(file_location)
        os.remove(xml_location)
        print("tmp files removed")
        return JSONResponse(status_code=200, content=res)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Could not save file")
