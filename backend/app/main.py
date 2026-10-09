import logging

from fastapi import FastAPI

from app.routes.prediction import router as prediction_router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is running"
    }


app.include_router(prediction_router)