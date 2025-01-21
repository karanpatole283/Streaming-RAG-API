from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse
from app.schemas import QueryRequest, QueryResponse
from app.rag_pipeline import RAGPipeline
from app.logger import log_request
import asyncio


app = FastAPI()


pipeline = RAGPipeline()

@app.post("/query", response_model=QueryResponse)
async def query_endpoint(request: QueryRequest):
    
    log_request(request.model_dump())
    try:
        async def generate_response():
            
            async for chunk in pipeline.stream_query(request.query, request.top_k):
                yield chunk
        return StreamingResponse(generate_response(), media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/")
async def root():
    return {"message": "Welcome to the Streaming RAG API!"}


