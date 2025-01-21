import asyncio

class RAGPipeline:
    def __init__(self):
        
        self.datastore = {
            "python": "Python is a versatile programming language.",
            "fastapi": "FastAPI is a modern framework for building APIs.",
            "pydantic": "Pydantic is used for data validation in Python.",
        }

    def retrieve(self, query: str, top_k: int):
       
        return [
            value for key, value in self.datastore.items() if key in query.lower()
        ][:top_k]

    async def stream_query(self, query: str, top_k: int):
        
        contexts = self.retrieve(query, top_k)
        for context in contexts:
            await asyncio.sleep(1)  
            yield context + "\n"
