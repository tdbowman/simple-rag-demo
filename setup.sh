#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting RAG System Setup...${NC}"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}Python 3 is not installed. Please install Python 3.8 or higher.${NC}"
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo -e "${YELLOW}pip3 is not installed. Please install pip3.${NC}"
    exit 1
fi

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo -e "${YELLOW}Docker is not installed. Please install Docker.${NC}"
    exit 1
fi

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo -e "${YELLOW}Ollama is not installed. Please install Ollama from https://ollama.ai${NC}"
    exit 1
fi

# Create and activate virtual environment
echo -e "${GREEN}Creating virtual environment...${NC}"
python3 -m venv venv
source venv/bin/activate

# Install requirements
echo -e "${GREEN}Installing Python packages...${NC}"
pip install -r requirements.txt

# Pull Llama model
echo -e "${GREEN}Pulling Llama 2 model...${NC}"
ollama pull llama2:1.3b

# Start Qdrant
echo -e "${GREEN}Starting Qdrant...${NC}"
docker run -d -p 6333:6333 qdrant/qdrant

echo -e "${GREEN}Setup complete!${NC}"
echo -e "${YELLOW}To start the application, run:${NC}"
echo -e "source venv/bin/activate"
echo -e "streamlit run app.py" 