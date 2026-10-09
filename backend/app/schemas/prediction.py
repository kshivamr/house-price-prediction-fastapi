from pydantic import BaseModel, Field


class HouseData(BaseModel):
    area: int = Field(gt=0)
    bedrooms: int = Field(gt=0)
    bathrooms: int = Field(gt=0)
    stories: int = Field(gt=0)

    mainroad: str
    guestroom: str
    basement: str
    hotwaterheating: str
    airconditioning: str

    parking: int = Field(ge=0)
    prefarea: str
    furnishingstatus: str


class PredictionResponse(BaseModel):
    predicted_price: float
    currency: str
    message: str