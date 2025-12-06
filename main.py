import uvicorn

from src.fastapi.service import mlops_app


def main():
    uvicorn.run(
        app=mlops_app,
        host="0.0.0.0",
        port=8080
    )    


if __name__ == "__main__":
    main()
