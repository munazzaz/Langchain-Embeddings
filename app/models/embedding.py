from pydantic import BaseModel
from typing import List

class TextInput(BaseModel):
    text: str

class EmbeddingResponse(BaseModel):
    text: str
    embedding: List[float]

class CompareTextInput(BaseModel):
    text_1: str
    text_2: str

class SimilarityResponse(BaseModel):
    text_1: str
    text_2: str
    cosine_similarity: float