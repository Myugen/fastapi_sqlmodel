from fastapi import APIRouter, HTTPException

from models.item import ItemOut, ItemPagination

router = APIRouter()


@router.get('/', response_model=ItemPagination)
def find_items(offset: int = 0, limit: int = 10):
    total = 50
    if offset * limit < total:
        return ItemPagination(offset=offset, limit=limit, total=total, data=[])
    else:
        raise HTTPException(status_code=404, detail='Items not found')


@router.get('/{item_id}', response_model=ItemOut)
def get_item(item_id: str):
    return ItemOut(id=item_id)
