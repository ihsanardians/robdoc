from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    description="Business Document Automation Platform",
    version="0.1.0",
    debug=settings.debug,
)


@app.get("/")
def root():
    return {
        "message": f"{settings.app_name} is running",
        "environment": settings.app_env,
        "status": "success",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "environment": settings.app_env,
    }