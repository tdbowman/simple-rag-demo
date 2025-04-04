# PowerShell script for RAG System Setup

Write-Host "Starting RAG System Setup..." -ForegroundColor Green

# Check if Python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Please install Python 3.8 or higher." -ForegroundColor Yellow
    exit 1
}

# Check if pip is installed
if (-not (Get-Command pip -ErrorAction SilentlyContinue)) {
    Write-Host "pip is not installed. Please install pip." -ForegroundColor Yellow
    exit 1
}

# Check if Docker is installed
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "Docker is not installed. Please install Docker Desktop for Windows." -ForegroundColor Yellow
    exit 1
}

# Check if Ollama is installed
if (-not (Get-Command ollama -ErrorAction SilentlyContinue)) {
    Write-Host "Ollama is not installed. Please install Ollama from https://ollama.ai" -ForegroundColor Yellow
    exit 1
}

# Create and activate virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Green
python -m venv venv

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Green
.\venv\Scripts\Activate.ps1

# Upgrade pip
Write-Host "Upgrading pip..." -ForegroundColor Green
pip install --upgrade pip

# Install requirements
Write-Host "Installing Python packages..." -ForegroundColor Green
pip install -r requirements.txt

# Pull Llama model
Write-Host "Pulling Llama 2 model..." -ForegroundColor Green
ollama pull llama2:1.3b

# Start Qdrant
Write-Host "Starting Qdrant..." -ForegroundColor Green
docker run -d -p 6333:6333 qdrant/qdrant

Write-Host "Setup complete!" -ForegroundColor Green
Write-Host "To start the application, run:" -ForegroundColor Yellow
Write-Host ".\venv\Scripts\Activate.ps1"
Write-Host "streamlit run app.py"

# Create a start script
Write-Host "Creating start script..." -ForegroundColor Green
@"
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Start Streamlit app
streamlit run app.py
"@ | Out-File -FilePath "start.ps1" -Encoding UTF8

Write-Host "You can now start the application by running:" -ForegroundColor Green
Write-Host ".\start.ps1" 