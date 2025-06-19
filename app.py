from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Wczytaj dane i trenuj model
df = pd.read_csv("synthetic_cardio_data.csv")
X = df[[
    "age", "heart_rate", "sbp", "dbp", "spo2",
    "dyspnea", "fatigue", "edema", "chf",
    "arrhythmia", "ischemic_hd", "prior_hospitalizations"
]]
y = df["mortality_30d"]
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

app = FastAPI()

class Patient(BaseModel):
    age: int
    heart_rate: int
    sbp: int
    dbp: int
    spo2: int
    dyspnea: int
    fatigue: int
    edema: int
    chf: int
    arrhythmia: int
    ischemic_hd: int
    prior_hospitalizations: int

@app.post("/predict")
def predict_mortality(patient: Patient):
    input_data = pd.DataFrame([patient.dict()])
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]
    return {
        "prediction": "Zgon w 30 dni" if prediction == 1 else "Brak zgonu",
        "risk": round(proba * 100, 2)
    }
