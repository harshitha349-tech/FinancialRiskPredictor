from pathlib import Path
import joblib, pandas as pd
import shap
ROOT=Path(__file__).resolve().parents[2]
model=joblib.load(ROOT/'models/creditlens_model.joblib')

def explain(data):
    pipe=model
    pre=pipe.named_steps['preprocessor']; estimator=pipe.named_steps['model']
    X=pd.DataFrame([data])
    Xt=pre.transform(X)
    names=list(pre.get_feature_names_out())
    explainer=shap.TreeExplainer(estimator)
    vals=explainer.shap_values(Xt)
    if isinstance(vals,list): vals=vals[0]
    vals=vals[0] if getattr(vals,'ndim',1)>1 else vals
    grouped={}
    for name,val in zip(names,vals):
        raw=name.split('__',1)[-1]
        base=raw.split('_',1)[0] if raw not in data else raw
        # Match one-hot columns back to the original feature name.
        for col in data:
            if raw==col or raw.startswith(col+'_'):
                base=col; break
        grouped[base]=grouped.get(base,0)+float(val)
    items=sorted(grouped.items(),key=lambda x:x[1],reverse=True)
    positive=[{'feature':k,'impact':round(v,3),'direction':'increases risk','message':f"{k.replace('_',' ').title()} increased the predicted risk."} for k,v in items if v>0][:4]
    negative=[{'feature':k,'impact':round(v,3),'direction':'reduces risk','message':f"{k.replace('_',' ').title()} reduced the predicted risk."} for k,v in reversed(items) if v<0][:4]
    return {'factors_increasing_risk':positive,'factors_reducing_risk':negative,'all_contributions':[{'feature':k,'impact':round(v,3)} for k,v in items[:10]]}
