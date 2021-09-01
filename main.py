from fastapi import FastAPI

from api.v1.router import api_v1_router

app = FastAPI(title="FastAPI Sample Project")


app.include_router(api_v1_router, prefix="/api/v1")
