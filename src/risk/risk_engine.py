"""Transparent, rule-based risk dimensions used alongside the ML prediction."""

def clamp(v): return max(0, min(100, round(float(v))))

def calculate_dimensions(a):
    default = clamp(a.get("default_probability", 0) * 100)
    checking = a.get("checking_status", "no checking")
    history = a.get("credit_history", "existing paid")
    duration = float(a.get("duration", 12))
    amount = float(a.get("credit_amount", 5000))
    savings = a.get("savings_status", "500<=X<1000")
    employment = a.get("employment", "1<=X<4")
    installment = float(a.get("installment_commitment", 2))
    age = float(a.get("age", 35))
    existing = float(a.get("existing_credits", 2))
    housing = a.get("housing", "own")

    repayment = 25 + (duration > 36)*22 + (installment >= 4)*25 + (amount > 8000)*18
    stress = 20 + (checking == "<0")*30 + (savings in ["<100", "unknown"])*25 + (employment in ["unemployed", "<1"])*25
    stability = 20 + (history in ["critical", "poor"])*35 + (employment in ["unemployed", "<1"])*20 + (age < 25)*10
    exposure = 20 + (amount > 8000)*35 + (duration > 36)*25 + (existing >= 4)*15 + (housing == "rent")*5
    return {
        "default_risk": clamp(default),
        "repayment_capacity": clamp(repayment),
        "financial_stress": clamp(stress),
        "credit_stability": clamp(stability),
        "debt_exposure": clamp(exposure),
    }

def overall_score(dimensions):
    # Higher means greater estimated risk, matching the product's 0–100 risk scale.
    score = (
        dimensions["default_risk"]*.35 +
        dimensions["repayment_capacity"]*.18 +
        dimensions["financial_stress"]*.18 +
        dimensions["credit_stability"]*.12 +
        dimensions["debt_exposure"]*.17
    )
    return clamp(score)

def category(score):
    if score < 25: return "Low"
    if score < 50: return "Medium"
    if score < 75: return "High"
    return "Very High"
