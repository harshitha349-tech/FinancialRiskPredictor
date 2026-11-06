from src.risk.risk_engine import category

def monitor(history):
    if len(history)<2: return {'current':history[-1] if history else None,'previous':None,'change':0,'warning':None}
    cur=history[-1]; prev=history[-2]; change=cur['risk_score']-prev['risk_score']
    warning = change <= -10
    return {'current':cur,'previous':prev,'change':change,'warning':warning,'message':'Applicant risk has increased significantly compared with the previous assessment.' if warning else 'No significant deterioration detected.'}
