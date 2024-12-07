from langchain.text_splitter import RecursiveCharacterTextSplitter

def preprocess_text(text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> list[str]:
    """
    Splits the text into smaller chunks for embedding or processing.
    
    Args:
        text (str): The extracted text to preprocess.
        chunk_size (int): Maximum size of each text chunk.
        chunk_overlap (int): Overlap size between chunks.
    
    Returns:
        list[str]: A list of text chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)
