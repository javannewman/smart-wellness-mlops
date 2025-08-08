from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
instrumentator = Instrumentator().instrument(app).expose(app)

model = joblib.load("models/model.joblib")

class InputData(BaseModel):
    heart_rate: float
    sleep_hours: float
    steps: int

@app.post("/predict")
def predict(data: InputData):
    df = pd.DataFrame([data.dict()])
    pred = model.predict(df)[0]
    return {"wellness_score": round(pred, 2)}
