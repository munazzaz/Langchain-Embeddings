from fastapi import APIRouter, HTTPException
from app.models.embedding import TextInput, EmbeddingResponse, CompareTextInput, SimilarityResponse
from app.utils.embedding import generate_embedding, calculate_cosine_similarity

router = APIRouter()

# In-memory store for embeddings
embedding_store = {}

@router.get("/")
async def get_embedding():
    return {"message": "This is the embeddings route"}


@router.post("/generate-embedding", response_model=EmbeddingResponse)
def create_embedding(input: TextInput):
    try:
       
        embedding = generate_embedding(input.text)
        
        embedding_store[input.text] = embedding
        
        return {"text": input.text, "embedding": embedding}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# Endpoint to verify if embedding is being generating correctly
@router.post("/compare-similarity", response_model=SimilarityResponse)
def compare_similarity(input: CompareTextInput):
    """
    Endpoint to calculate cosine similarity between two texts.
    """
    try:
        
        embedding_1 = generate_embedding(input.text_1)
        embedding_2 = generate_embedding(input.text_2)
        
        similarity = calculate_cosine_similarity(embedding_1, embedding_2)
        
        return {
            "text_1": input.text_1,
            "text_2": input.text_2,
            "cosine_similarity": similarity
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
