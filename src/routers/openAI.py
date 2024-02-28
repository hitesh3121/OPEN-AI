from fastapi import APIRouter
from src.controller.openAI import openAI_API

router = APIRouter()


@router.get("/")
async def openAICalled():
    response = await openAI_API()
    return response
