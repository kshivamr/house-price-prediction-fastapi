import pandas as pd

from fastapi import APIRouter, HTTPException

from app.schemas.prediction import HouseData, PredictionResponse
from app.services.model_service import predict_price


router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(house: HouseData):

    try:

        house_data = pd.DataFrame([{
            "area": house.area,
            "bedrooms": house.bedrooms,
            "bathrooms": house.bathrooms,
            "stories": house.stories,
            "mainroad": house.mainroad,
            "guestroom": house.guestroom,
            "basement": house.basement,
            "hotwaterheating": house.hotwaterheating,
            "airconditioning": house.airconditioning,
            "parking": house.parking,
            "prefarea": house.prefarea,
            "furnishingstatus": house.furnishingstatus
        }])

        prediction = predict_price(house_data)

        return {
            "predicted_price": prediction,
            "currency": "INR",
            "message": "House price predicted successfully"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )