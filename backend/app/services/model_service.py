import logging
import joblib
from pathlib import Path


logger = logging.getLogger(__name__)


# Find project root
BASE_DIR = Path(__file__).resolve().parents[3]

# Path to trained model
MODEL_PATH = BASE_DIR / "ml_model" / "model.pkl"


# Load model
model = joblib.load(MODEL_PATH)

logger.info("ML model loaded successfully")


def predict_price(house_data):

    logger.info("Making house price prediction")

    prediction = model.predict(house_data)

    logger.info("Prediction completed successfully")

    return prediction[0]