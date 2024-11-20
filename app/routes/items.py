from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_items():
    return {"message": "List of items"}

@router.post("/")
async def create_item(item: dict):
    return {"message": f"Item {item['name']} created"}
