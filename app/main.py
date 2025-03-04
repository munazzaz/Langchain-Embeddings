from fastapi import FastAPI
from app.routes.items import router as items_router
from app.routes import users, items, embedding


app = FastAPI(
    title="Xenara FastAPI",
    description="API documentation for Xenara FastAPI services",
    version="1.0.0",
    contact={
        "name": "Xenara Team",
        "email": "support@xenara.ai",
    }
)

# Include routes
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(items_router, prefix="/api")
app.include_router(embedding.router, prefix="/embeddings", tags=["Embeddings"] )



@app.get("/")
async def root():
    """
    Root endpoint of the API
    """
    return {"message": "Welcome to Xenara FastAPI!"}
