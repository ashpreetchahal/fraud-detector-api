from pydantic import BaseModel
from typing import Optional

class Transaction(BaseModel):
    transaction_id: str
    user_id: str
    amount: float
    location: Optional[str] = None
    timestamp: Optional[str] = None

class FraudResponse(BaseModel):
    transaction_id: str
    is_fraud: bool
    reason: Optional[str] = None