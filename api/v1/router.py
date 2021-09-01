from fastapi import APIRouter

from api.v1.routes import items

api_v1_router = APIRouter()
api_v1_router.include_router(items.router, prefix='/items', tags=['items'])
