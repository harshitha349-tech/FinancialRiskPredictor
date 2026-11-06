from pydantic import BaseModel, Field
from typing import Optional
class CreditProfile(BaseModel):
    applicant_id: str = Field(min_length=2,max_length=40)
    checking_status: str; duration: int = Field(ge=4,le=72); credit_history: str; purpose: str
    credit_amount: float = Field(gt=0,le=100000); savings_status: str; employment: str
    installment_commitment: int = Field(ge=1,le=4); personal_status: str; other_parties: str
    residence_since: int = Field(ge=1,le=4); property_magnitude: str; age: int = Field(ge=18,le=90)
    other_payment_plans: str; housing: str; existing_credits: int = Field(ge=1,le=10)
    job: str; num_dependents: int = Field(ge=1,le=5); own_telephone: str; foreign_worker: str
class SimulationRequest(BaseModel):
    profile: CreditProfile
    changes: dict
class MonitoringRequest(BaseModel):
    applicant_id: str
