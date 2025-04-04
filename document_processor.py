"""
Document Processor Module

This module handles the loading and processing of different types of documents
(PDF, TXT, and web content) for the RAG system.
"""

import os
from typing import List, Union
from langchain_community.document_loaders import PyPDFLoader, TextLoader, WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

class DocumentProcessor:
    """
    A class to handle document loading and processing for the RAG system.
    Supports PDF, TXT files, and web URLs.
    """
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Initialize the DocumentProcessor.
        
        Args:
            chunk_size (int): Size of text chunks for splitting documents
            chunk_overlap (int): Overlap between chunks
        """
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )
    
    def process_file(self, file_path: str) -> List[Document]:
        """
        Process a file (PDF or TXT) and return chunks of text.
        
        Args:
            file_path (str): Path to the file to process
            
        Returns:
            List[Document]: List of document chunks
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        file_extension = os.path.splitext(file_path)[1].lower()
        
        if file_extension == '.pdf':
            loader = PyPDFLoader(file_path)
        elif file_extension == '.txt':
            loader = TextLoader(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
            
        documents = loader.load()
        return self.text_splitter.split_documents(documents)
    
    def process_url(self, url: str) -> List[Document]:
        """
        Process a URL and return chunks of text from the web page.
        
        Args:
            url (str): URL to process
            
        Returns:
            List[Document]: List of document chunks
        """
        loader = WebBaseLoader(url)
        documents = loader.load()
        return self.text_splitter.split_documents(documents)
    
    def process_documents(self, inputs: List[Union[str, bytes]]) -> List[Document]:
        """
        Process multiple documents (files or URLs).
        
        Args:
            inputs (List[Union[str, bytes]]): List of file paths or URLs
            
        Returns:
            List[Document]: Combined list of document chunks
        """
        all_chunks = []
        
        for input_item in inputs:
            if isinstance(input_item, str):
                if input_item.startswith(('http://', 'https://')):
                    chunks = self.process_url(input_item)
                else:
                    chunks = self.process_file(input_item)
                all_chunks.extend(chunks)
                
        return all_chunks 