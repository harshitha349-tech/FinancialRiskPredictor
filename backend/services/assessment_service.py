from src.models.predictor import predict
from src.risk.risk_engine import calculate_dimensions, overall_score, category
from src.recommendation.engine import recommendation
from src.explainability.explainer import explain

def assess(profile):
    data=dict(profile); data.pop('applicant_id',None)
    pred=predict(data); dims=calculate_dimensions({**data,**pred}); score=overall_score(dims); cat=category(score)
    return {'applicant_id':profile['applicant_id'],'profile':profile,'risk_score':score,'category':cat,'default_probability':pred['default_probability'],'dimensions':dims,'explanation':explain(data),'recommendation':recommendation(cat,dims)}
