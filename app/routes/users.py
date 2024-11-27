from fastapi import APIRouter
from app.models.users import User

router = APIRouter()

@router.get("/")
async def get_users():
    """Retrieve all users."""
    return {"message": "List of users"}

@router.post("/")
async def create_user(user: User):
    """Create a new user."""
    return {"message": f"User '{user.name}' created with email {user.email}"}
