import uvicorn

from config import SERVICE_PORT
from src.fastapi.service import mlops_app


def main():
    uvicorn.run(
        app=mlops_app,
        host="0.0.0.0",
        port=SERVICE_PORT
    )    


if __name__ == "__main__":
    main()
