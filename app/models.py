from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class FraudLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str
    amount: float
    timestamp: datetime
    location: str
    is_fraud: bool
    logged_at: datetime = Field(default_factory=datetime.utcnow)