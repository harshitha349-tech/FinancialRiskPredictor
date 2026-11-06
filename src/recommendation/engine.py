def recommendation(category, dimensions):
    if category == "Low":
        text="Suitable for standard lending evaluation, subject to normal verification."
        action="Proceed with standard human review."
    elif category == "Medium":
        text="Moderate risk suggests reviewing affordability and existing obligations before final terms are considered."
        action="Consider additional verification or modified loan terms."
    elif category == "High":
        text="Elevated risk is driven by one or more financial stress, repayment, or exposure indicators."
        action="Manual review is recommended before a lending decision."
    else:
        text="The current profile indicates substantial estimated default risk and financial pressure."
        action="Do not rely on the model alone; conduct detailed manual assessment."
    reasons=[]
    labels={"default_risk":"predicted default risk","repayment_capacity":"repayment burden","financial_stress":"financial stress","credit_stability":"credit stability","debt_exposure":"debt exposure"}
    for k,v in sorted(dimensions.items(),key=lambda x:x[1],reverse=True)[:3]:
        if v>=60: reasons.append(f"High {labels[k]} ({v}/100)")
    if not reasons: reasons.append("No single risk dimension is strongly elevated.")
    return {"recommendation":text,"next_action":action,"reasons":reasons}
