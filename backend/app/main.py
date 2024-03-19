import os

from fastapi import FastAPI
from .routers import catalog_api, analysis_api
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(catalog_api.router)
app.include_router(analysis_api.router)


@app.get("/",
         summary="API Root",
         description="This is the root endpoint of the API. It serves as an initial point to check the API status "
                     "and discover the base URI.",
         response_description="Provides a welcome message and the base URI of the API.")
async def root():
    """
    The API's root endpoint.

    This endpoint offers a simple JSON response that includes the base URI for the API and a message welcoming the
    user. It's an excellent starting point to explore the API's features.
    """
    return {"uri": "/"}


if __name__ == '__main__':
    import uvicorn
    os.environ["TEST_MODE"] = "True"
    uvicorn.run(app, host="localhost", port=8000)
