"""
RAG System Module

This module implements the core Retrieval-Augmented Generation system
that combines document retrieval with language model generation.
"""

from typing import List
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from document_processor import DocumentProcessor
from vector_store import VectorStore

class RAGSystem:
    """
    A class that implements a complete RAG system using Ollama and Qdrant.
    """
    
    def __init__(self):
        """
        Initialize the RAG system with document processor and vector store.
        """
        self.document_processor = DocumentProcessor()
        self.vector_store = VectorStore()
        self.llm = Ollama(model="llama2:1.3b")
        
        # Create a custom prompt template
        self.prompt_template = """Use the following pieces of context to answer the question at the end.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.

        Context: {context}

        Question: {question}

        Answer: """
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.vector_store.as_retriever(),
            return_source_documents=True,
            chain_type_kwargs={
                "prompt": PromptTemplate(
                    template=self.prompt_template,
                    input_variables=["context", "question"]
                )
            }
        )
    
    def add_documents(self, inputs: List[str]) -> None:
        """
        Add documents to the knowledge base.
        
        Args:
            inputs (List[str]): List of file paths or URLs
        """
        documents = self.document_processor.process_documents(inputs)
        self.vector_store.add_documents(documents)
    
    def query(self, question: str) -> dict:
        """
        Query the RAG system with a question.
        
        Args:
            question (str): The question to ask
            
        Returns:
            dict: Response containing answer and source documents
        """
        result = self.qa_chain({"query": question})
        return {
            "answer": result["result"],
            "sources": result["source_documents"]
        }
    
    def clear_knowledge_base(self) -> None:
        """
        Clear all documents from the knowledge base.
        """
        self.vector_store.clear_collection() 