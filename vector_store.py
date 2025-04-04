"""
Vector Store Module

This module manages the Qdrant vector database for storing and retrieving document embeddings.
"""

from typing import List
from qdrant_client import QdrantClient
from qdrant_client.http import models
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Qdrant
from langchain.schema import Document

class VectorStore:
    """
    A class to manage the Qdrant vector database for the RAG system.
    Handles document storage and retrieval using embeddings.
    """
    
    def __init__(self, collection_name: str = "documents"):
        """
        Initialize the VectorStore.
        
        Args:
            collection_name (str): Name of the Qdrant collection
        """
        self.collection_name = collection_name
        self.client = QdrantClient("localhost", port=6333)
        self.embeddings = OllamaEmbeddings(model="llama2")
        
        # Create collection if it doesn't exist
        try:
            self.client.get_collection(collection_name)
        except:
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(
                    size=4096,  # Size of Llama 2 embeddings
                    distance=models.Distance.COSINE
                )
            )
        
        self.vector_store = Qdrant(
            client=self.client,
            collection_name=collection_name,
            embeddings=self.embeddings
        )
    
    def add_documents(self, documents: List[Document]) -> None:
        """
        Add documents to the vector store.
        
        Args:
            documents (List[Document]): List of documents to add
        """
        self.vector_store.add_documents(documents)
    
    def similarity_search(self, query: str, k: int = 4) -> List[Document]:
        """
        Search for similar documents to the query.
        
        Args:
            query (str): Search query
            k (int): Number of results to return
            
        Returns:
            List[Document]: List of similar documents
        """
        return self.vector_store.similarity_search(query, k=k)
    
    def clear_collection(self) -> None:
        """
        Clear all documents from the collection.
        """
        self.client.delete_collection(self.collection_name)
        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=models.VectorParams(
                size=4096,
                distance=models.Distance.COSINE
            )
        ) 