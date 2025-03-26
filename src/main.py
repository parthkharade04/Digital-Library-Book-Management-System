import os
import uvicorn
from fastapi import FastAPI
from src.routes.book_routes import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Get port from environment
    uvicorn.run(app, host="0.0.0.0", port=port)
