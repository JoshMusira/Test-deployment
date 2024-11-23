# app/main.py

from fastapi import FastAPI
from routes.sample import router

app = FastAPI(
    title="My FastAPI App",
    description="This is a sample FastAPI app",
)

# Include the routes from sample.py
app.include_router(router)

# Root route
@app.get("/")
async def root():
    return {"message": "Welcome to My FastAPI App!"}
