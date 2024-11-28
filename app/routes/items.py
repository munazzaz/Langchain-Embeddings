from fastapi import APIRouter
from app.models.items import Item

router = APIRouter()

@router.get("/")
async def get_items():
    """Retrieve all items."""
    return {"message": "List of items"}

@router.post("/")
async def create_item(item: Item):
    """Create a new item."""
    return {"message": f"Item '{item.name}' created with price {item.price}"}
