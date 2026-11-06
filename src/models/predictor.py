from pathlib import Path
import joblib, pandas as pd
ROOT=Path(__file__).resolve().parents[2]
MODEL_PATH=ROOT/'models/creditlens_model.joblib'
model=joblib.load(MODEL_PATH)

def predict(data):
    df=pd.DataFrame([data])
    p=float(model.predict_proba(df)[0,1])
    return {'default_probability':p,'model_prediction':'bad' if p>=0.5 else 'good'}
