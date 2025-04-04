"""
Streamlit Application

This module provides a user-friendly interface for the RAG system
using Streamlit.
"""

import streamlit as st
import tempfile
import os
from rag_system import RAGSystem

# Initialize the RAG system
@st.cache_resource
def get_rag_system():
    return RAGSystem()

# Set up the Streamlit interface
st.set_page_config(
    page_title="Simple RAG System Demo",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Simple RAG System Demo")
st.markdown("""
This demo shows how a Retrieval-Augmented Generation (RAG) system works.
You can upload documents or add URLs, and then ask questions about their content.
""")

# Initialize session state
if 'rag_system' not in st.session_state:
    st.session_state.rag_system = get_rag_system()
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = []
if 'urls' not in st.session_state:
    st.session_state.urls = []

# Sidebar for document upload and URL input
with st.sidebar:
    st.header("Add Documents")
    
    # File upload
    uploaded_files = st.file_uploader(
        "Upload PDF or TXT files",
        type=['pdf', 'txt'],
        accept_multiple_files=True
    )
    
    # URL input
    url = st.text_input("Add a URL to scrape")
    if url and st.button("Add URL"):
        if url not in st.session_state.urls:
            st.session_state.urls.append(url)
    
    # Display current documents
    st.subheader("Current Documents")
    if st.session_state.uploaded_files:
        st.write("Uploaded Files:")
        for file in st.session_state.uploaded_files:
            st.write(f"- {file}")
    
    if st.session_state.urls:
        st.write("URLs:")
        for url in st.session_state.urls:
            st.write(f"- {url}")
    
    # Clear documents button
    if st.button("Clear All Documents"):
        st.session_state.rag_system.clear_knowledge_base()
        st.session_state.uploaded_files = []
        st.session_state.urls = []
        st.rerun()

# Process new documents
if uploaded_files:
    for file in uploaded_files:
        if file.name not in st.session_state.uploaded_files:
            # Save uploaded file to temporary directory
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.name)[1]) as tmp_file:
                tmp_file.write(file.getvalue())
                tmp_file_path = tmp_file.name
            
            # Add to RAG system
            st.session_state.rag_system.add_documents([tmp_file_path])
            st.session_state.uploaded_files.append(file.name)
            
            # Clean up temporary file
            os.unlink(tmp_file_path)

# Process new URLs
if st.session_state.urls:
    st.session_state.rag_system.add_documents(st.session_state.urls)

# Main chat interface
st.header("Chat with Your Documents")

# Chat input
user_input = st.text_input("Ask a question about your documents:")

if user_input:
    with st.spinner("Thinking..."):
        response = st.session_state.rag_system.query(user_input)
        
        # Display answer
        st.subheader("Answer")
        st.write(response["answer"])
        
        # Display sources
        if response["sources"]:
            st.subheader("Sources")
            for i, doc in enumerate(response["sources"], 1):
                st.write(f"Source {i}:")
                st.text(doc.page_content[:200] + "...") 