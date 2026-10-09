# House Price Prediction API

An end-to-end Machine Learning project that predicts house prices using **Linear Regression** and exposes the trained model through a **FastAPI REST API**.

## 🚀 Project Overview

This project takes house-related information such as:

- Area
- Number of bedrooms
- Number of bathrooms
- Number of stories
- Parking
- Main road
- Guest room
- Basement
- Air conditioning
- Hot water heating
- Preferred area
- Furnishing status

and predicts the estimated house price.

The project includes:

- Machine Learning model training
- Numerical and categorical feature preprocessing
- Model serialization using Joblib
- FastAPI backend
- Pydantic request validation
- Prediction endpoint
- API error handling
- Application logging

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Joblib
- FastAPI
- Uvicorn
- Pydantic

## 📁 Project Structure

```text
house_price_pridiction/
│
├── README.md
├── .gitignore
│
├── ml_model/
│   ├── data/
│   │   └── Housing.csv
│   ├── train.py
│   ├── predict.py
│   ├── model.pkl
│   └── requirements.txt
│
└── backend/
    ├── app/
    │   ├── main.py
    │   ├── routes/
    │   │   └── prediction.py
    │   ├── schemas/
    │   │   └── prediction.py
    │   └── services/
    │       └── model_service.py
    │
    └── requirements.txt
```

## 🤖 Machine Learning

The model uses **Linear Regression**.

### Features

Numerical features:

```text
area
bedrooms
bathrooms
stories
parking
```

Categorical features:

```text
mainroad
guestroom
basement
hotwaterheating
airconditioning
prefarea
furnishingstatus
```

Categorical features are converted using `OneHotEncoder`.

The preprocessing and model are combined using a Scikit-learn `Pipeline`.

## 📊 Model Performance

The model was evaluated using:

- MAE
- MSE
- RMSE
- R² Score

Current model performance:

| Metric |        Score |
| ------ | -----------: |
| MAE    |  ~₹9.70 lakh |
| RMSE   | ~₹13.25 lakh |
| R²     |      ~65.29% |

## 💾 Model Saving

After training, the complete ML pipeline is saved using Joblib:

```python
joblib.dump(model, "model.pkl")
```

The FastAPI application later loads this trained model:

```python
model = joblib.load(MODEL_PATH)
```

This allows the API to make predictions without retraining the model.

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd house_price_pridiction
```

### Install ML dependencies

```bash
cd ml_model
pip install -r requirements.txt
```

### Train the model

```bash
python train.py
```

This generates:

```text
model.pkl
```

### Install backend dependencies

Move to the backend directory:

```bash
cd ../backend
pip install -r requirements.txt
```

## 🚀 Run the API

From the `backend` directory:

```bash
uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can test the `/predict` endpoint directly from Swagger UI.

## 🔮 Prediction Endpoint

### POST `/predict`

Example request:

```json
{
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
}
```

Example response:

```json
{
  "predicted_price": 7397231.619397208,
  "currency": "INR",
  "message": "House price predicted successfully"
}
```

## 🔄 Application Flow

```text
Client
   ↓
POST /predict
   ↓
Pydantic Validation
   ↓
Prediction Route
   ↓
Pandas DataFrame
   ↓
ML Model Service
   ↓
model.pkl
   ↓
Prediction
   ↓
JSON Response
```

## 📝 Logging

The application also uses Python logging to track important events such as:

```text
ML model loaded successfully
Making house price prediction
Prediction completed successfully
```

Logs can be viewed in the terminal where Uvicorn is running.

## 🎯 Future Improvements

- Try advanced regression models
- Hyperparameter tuning
- Improve model accuracy
- Add database integration
- Add frontend interface
- Add Docker support
- Deploy the API to the cloud
- Add automated testing
- Add CI/CD pipeline

## 👨‍💻 Author

**Shivam Kumar**

Built as an end-to-end Machine Learning + FastAPI project.
