FEATURE_COLUMNS = [
    'checking_status','duration','credit_history','purpose','credit_amount','savings_status','employment',
    'installment_commitment','personal_status','other_parties','residence_since','property_magnitude','age',
    'other_payment_plans','housing','existing_credits','job','num_dependents','own_telephone','foreign_worker'
]

def validate_features(data):
    missing=[c for c in FEATURE_COLUMNS if c not in data]
    if missing: raise ValueError(f"Missing fields: {', '.join(missing)}")
    return {c:data[c] for c in FEATURE_COLUMNS}
