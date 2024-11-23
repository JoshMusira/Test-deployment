# app/routes/sample.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

@router.get("/greet/{name}")
async def greet_user(name: str):
    return {"message": f"Hello, {name}!"}
