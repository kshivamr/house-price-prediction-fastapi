import pandas as pd
import joblib


# Load trained model
model = joblib.load("model.pkl")


# Create one new house
house = pd.DataFrame([{
    "area": 5000,
    "bedrooms": 4,
    "bathrooms": 2,
    "stories": 3,
    "mainroad": "yes",
    "guestroom": "no",
    "basement": "no",
    "hotwaterheating": "no",
    "airconditioning": "yes",
    "parking": 2,
    "prefarea": "yes",
    "furnishingstatus": "furnished"
}])


# Make prediction
prediction = model.predict(house)


print("Predicted House Price:", prediction[0])