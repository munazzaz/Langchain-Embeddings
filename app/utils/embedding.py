import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from langchain_huggingface import HuggingFaceEmbeddings
from app.config import settings

# Load the embedding model
embedding_model = HuggingFaceEmbeddings(model_name=settings.hugging_face_model)

def preprocess_text(text: str) -> str:
    """
    Preprocess the input text by performing operations such as
    lowercasing, removing special characters, etc.
    """
    
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text) 
    text = re.sub(r'\s+', ' ', text).strip()  
    return text

def generate_embedding(text: str):
    try:
      
        preprocessed_text = preprocess_text(text)
        
        # Log: To verify if text is preprocessed
        # print(f"Original Text: '{text}'")
        # print(f"Preprocessed Text: '{preprocessed_text}'")
        
        embedding = embedding_model.embed_query(preprocessed_text)
        return embedding
    except Exception as e:
        print(f"Error generating embedding: {e}")
        return None


# To verify if embedding is being generating correctly
def calculate_cosine_similarity(embedding_1: list[float], embedding_2: list[float]) -> float:
    
    if len(embedding_1) != len(embedding_2):
        raise ValueError("Embeddings must have the same dimension")
   
    vector_1 = np.array(embedding_1).reshape(1, -1)
    vector_2 = np.array(embedding_2).reshape(1, -1)
   
    return float(cosine_similarity(vector_1, vector_2)[0][0])
