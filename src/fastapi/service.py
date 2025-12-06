from fastapi import FastAPI

from src.config import SERVICE_VERSION

mlops_app = FastAPI(
    version=SERVICE_VERSION
)

@mlops_app.get("/")
def home():
    return {"message": "Welcome to the Sid's MLOPs project"}
