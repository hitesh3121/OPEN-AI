import os
from fastapi import FastAPI
from src.routers.api import router as api_route
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from src.errors.http_error import http_error_handler

app = FastAPI()

OPENAI_KEY = os.getenv("OPEN_AI_KEY")


def get_application() -> FastAPI:
    applications = FastAPI()
    applications.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    applications.add_exception_handler(HTTPException, http_error_handler)
    applications.include_router(api_route, prefix="/api")

    return applications


app = get_application()
