from fastapi import APIRouter
from src.routers import openAI

router = APIRouter()

router.include_router(openAI.router, prefix="/openAI", tags=["OpenAI"])
