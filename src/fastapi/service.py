from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from src.config import SERVICE_VERSION

mlops_app = FastAPI(
    version=SERVICE_VERSION
)

@mlops_app.get("/")
async def home() -> HTMLResponse:
    with open("static/index.html", "rb") as f:
        return HTMLResponse(content=f.read(), status_code=200)
