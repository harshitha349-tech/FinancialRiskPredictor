from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import init_db, upsert_applicant, save_assessment, history, conn
from backend.routes.api import router
from backend.services.assessment_service import assess
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
app=FastAPI(title='CreditLens API',description='Adaptive & Explainable Credit Risk Intelligence',version='1.0.0')
app.add_middleware(CORSMiddleware,allow_origins=['*'],allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
app.include_router(router)
@app.on_event('startup')
def startup():
    init_db(); seed_demo()
@app.get('/')
def root(): return {'name':'CreditLens','tagline':'Adaptive & Explainable Credit Risk Intelligence','docs':'/docs'}
def seed_demo():
    df=pd.read_csv(ROOT/'data/demo/german_credit_synthetic.csv').sample(10,random_state=7)
    for _,row in df.iterrows():
        p=row.drop(labels=['class','applicant_id']).to_dict();
        # JSON-friendly numeric conversion
        p={k:(int(v) if hasattr(v,'item') and str(v).startswith(('int','uint')) else float(v) if hasattr(v,'item') and str(v).startswith('float') else v) for k,v in p.items()}
        p['applicant_id']=row['applicant_id']; result=assess(p); upsert_applicant(p['applicant_id'],p)
        if not history(p['applicant_id']):
            c=conn()
            # Seed a short historical trajectory so the monitoring screen is immediately demonstrable.
            base=result['risk_score']
            scores=[min(100,base+28),min(100,base+20),min(100,base+12),min(100,base+6),base]
            cats=['Very High' if s>=75 else 'High' if s>=50 else 'Medium' if s>=25 else 'Low' for s in scores]
            probs=[min(0.99,max(0.01,result['default_probability']+0.16)),min(0.99,max(0.01,result['default_probability']+0.11)),min(0.99,max(0.01,result['default_probability']+0.07)),min(0.99,max(0.01,result['default_probability']+0.03)),result['default_probability']]
            for s,cg,pr in zip(scores,cats,probs): c.execute('INSERT INTO risk_history(applicant_id,risk_score,category,default_probability,note) VALUES(?,?,?,?,?)',(p['applicant_id'],int(s),cg,float(pr),'Historical demonstration assessment'))
            c.commit(); c.close()
            save_assessment(p['applicant_id'],result)
