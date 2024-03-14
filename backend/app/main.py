from fastapi import FastAPI
<<<<<<< HEAD
from app.routers import catalog_api, analysis_api
from starlette.middleware.cors import CORSMiddleware
=======

from app.routers import catalog_api, analysis_api
>>>>>>> 648b214 (Make some changes in endpoint)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:5173",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(catalog_api.router)
app.include_router(analysis_api.router)


@app.get("/")
async def root():
    return {"uri": "/"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
