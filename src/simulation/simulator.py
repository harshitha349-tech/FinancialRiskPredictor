from src.models.predictor import predict
from src.risk.risk_engine import calculate_dimensions, overall_score, category

def simulate(current, changes):
    updated=dict(current)
    for k,v in changes.items():
        if v is not None: updated[k]=v
    before_pred=predict(current); after_pred=predict(updated)
    before_dim=calculate_dimensions({**current,**before_pred}); after_dim=calculate_dimensions({**updated,**after_pred})
    before_score=overall_score(before_dim); after_score=overall_score(after_dim)
    return {
      'before':{'risk_score':before_score,'default_probability':before_pred['default_probability'],'category':category(before_score)},
      'after':{'risk_score':after_score,'default_probability':after_pred['default_probability'],'category':category(after_score)},
      'score_change':after_score-before_score,
      'probability_change':after_pred['default_probability']-before_pred['default_probability'],
      'updated_profile':updated
    }
