from fastapi import FastAPI

from backend.app.routers import catalog_api, analysis_api

app = FastAPI()

app.include_router(catalog_api.router)
app.include_router(analysis_api.router)


@app.get("/")
async def root():
    return {"uri": "/"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


