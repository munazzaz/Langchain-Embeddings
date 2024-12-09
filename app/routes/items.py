from fastapi import APIRouter, HTTPException, UploadFile, File
from app.models.items import Item
from app.utils.helpers import preprocess_text, extract_text_from_pdf

router = APIRouter()

@router.get("/")
async def get_items():
    """Retrieve all items."""
    return {"message": "List of items"}

@router.post("/")
async def create_item(item: Item):
    """Create a new item."""
    return {"message": f"Item '{item.name}' created with price {item.price}"}

@router.post("/import-pdf")
async def import_pdf(pdf_file: UploadFile = File(...)):
    """
    Upload a PDF file and extract its text content.
    """
    if not pdf_file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    
    pdf_text = extract_text_from_pdf(pdf_file.file)
    if not pdf_text.strip():
        raise HTTPException(status_code=400, detail="PDF has no extractable text.")
    
    return {"message": "PDF processed successfully", "text_preview": pdf_text[:100]}

@router.post("/preprocess-text")
async def preprocess_text_route(extracted_text: str):
    """
    Preprocess extracted text by chunking it into smaller segments.
    
    Args:
        extracted_text (str): The raw text extracted from the PDF.
    
    Returns:
        dict: Preprocessing results, including chunks and their count.
    """
    try:
        if not extracted_text.strip():
            raise HTTPException(status_code=400, detail="Extracted text cannot be empty.")
        
        # Perform text chunking
        chunks = preprocess_text(extracted_text)
        
        return {
            "message": "Text preprocessing successful.",
            "chunk_count": len(chunks),
            "chunks": chunks[:2],  # Return a preview of the first two chunks
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")