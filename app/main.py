
from fastapi import FastAPI
from router import api_router
from starlette.middleware.cors import CORSMiddleware
from config import settings

app = FastAPI(
    title="Data Processing",
    version="1.0"
)

app.include_router(api_router)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )