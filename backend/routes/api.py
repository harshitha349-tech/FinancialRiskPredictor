from fastapi import APIRouter, HTTPException
import json
from backend.schemas import CreditProfile,SimulationRequest,MonitoringRequest
from backend.services.assessment_service import assess
from src.simulation.simulator import simulate
from src.monitoring.monitor import monitor
from backend.database import *
router=APIRouter(prefix='/api')
@router.get('/health')
def health(): return {'status':'healthy','service':'CreditLens API'}
@router.post('/predict')
def predict(profile:CreditProfile):
    result=assess(profile.model_dump()); upsert_applicant(profile.applicant_id,profile.model_dump()); save_assessment(profile.applicant_id,result); return result
@router.post('/simulate')
def simulation(req:SimulationRequest): return simulate(req.profile.model_dump(exclude={'applicant_id'}),req.changes)
@router.post('/recommend')
def recommend(profile:CreditProfile): return assess(profile.model_dump())['recommendation']
@router.post('/monitor')
def monitoring(req:MonitoringRequest):
    h=history(req.applicant_id)
    if not h: raise HTTPException(404,'Applicant history not found')
    return monitor(h)
@router.get('/applicants')
def applicants():
    out=[]
    for r in list_applicants():
        p=json.loads(r['profile_json']); out.append({'applicant_id':r['id'],'profile':p,'risk_score':r['risk_score'],'category':r['category'],'default_probability':r['default_probability'],'updated_at':r['created_at']})
    return out
@router.get('/applicants/{applicant_id}')
def applicant(applicant_id:str):
    r=get_applicant(applicant_id)
    if not r: raise HTTPException(404,'Applicant not found')
    return {'applicant_id':r['id'],'profile':json.loads(r['profile_json']),'history':history(applicant_id)}
@router.get('/risk-history/{applicant_id}')
def risk_history(applicant_id:str): return history(applicant_id)
@router.get('/model-metrics')
def model_metrics(): return json.load(open('models/model_metrics.json'))
@router.get('/dashboard')
def dashboard():
    rows=list_applicants(); recent=assessments(); cats={'Low':0,'Medium':0,'High':0,'Very High':0}
    for r in rows:
        if r['category']: cats[r['category']]=cats.get(r['category'],0)+1
    probs=[r['default_probability'] for r in rows if r['default_probability'] is not None]
    scores=[r['risk_score'] for r in rows if r['risk_score'] is not None]
    dim_totals={}; dim_count=0
    for r in recent:
        try:
            d=json.loads(r.get('dimensions_json') or '{}')
            for k,v in d.items(): dim_totals[k]=dim_totals.get(k,0)+v
            dim_count+=1
        except Exception: continue
    dims={k:round(v/dim_count) for k,v in dim_totals.items()} if dim_count else {}
    return {'total_applicants':len(rows),'risk_distribution':cats,'average_risk_score':round(sum(scores)/len(scores),1) if scores else 0,'average_default_probability':sum(probs)/len(probs) if probs else 0,'recent':recent,'risk_trend':[r['risk_score'] for r in reversed(recent) if r.get('risk_score') is not None],'dimension_comparison':dims}
