import sys, json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.models.predictor import predict
from src.risk.risk_engine import calculate_dimensions,overall_score,category
from src.recommendation.engine import recommendation
from src.explainability.explainer import explain
from src.simulation.simulator import simulate
import pandas as pd

def profile():
    r=pd.read_csv(Path(__file__).resolve().parents[1]/'data/demo/german_credit_synthetic.csv').iloc[0]
    return r.drop(labels=['class','applicant_id']).to_dict()

def test_prediction():
    r=predict(profile()); assert 0<=r['default_probability']<=1

def test_risk_score():
    p=profile(); pred=predict(p); d=calculate_dimensions({**p,**pred}); s=overall_score(d); assert 0<=s<=100; assert category(s) in ['Low','Medium','High','Very High']

def test_explanation():
    e=explain(profile()); assert e['factors_increasing_risk'] or e['factors_reducing_risk']

def test_recommendation():
    d={'default_risk':70,'repayment_capacity':65,'financial_stress':80,'credit_stability':40,'debt_exposure':70}; assert 'recommendation' in recommendation('High',d)

def test_simulation():
    p=profile(); r=simulate(p,{'credit_amount':2000}); assert 'before' in r and 'after' in r
