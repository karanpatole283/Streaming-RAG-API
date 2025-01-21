# Streaming RAG API Service

## Installation
1. Clone the repository:
   bash
   git clone <https://github.com/karanpatole283/Streaming-RAG-API>
   cd streaming_rag_service
## Install dependencies:
2. pip install -r requirements.txt

## uvicorn app.main:app --reload
3. uvicorn app.main:app --reload
## Usage
Open Swagger UI: http://127.0.0.1:8000/docs
POST /query:
{
  "query": "python",
  "top_k": 2
}

## Testing
Run tests using:
pytest


### **Step 4: Run the Service**
1. Start the API:
   ```bash
   uvicorn app.main:app --reload

## Open Swagger UI at http://127.0.0.1:8000/docs.
