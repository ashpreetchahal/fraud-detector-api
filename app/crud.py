from datetime import datetime
from sqlmodel import Session
from app.models import FraudLog

def log_transaction(session: Session, transaction: dict, is_fraud: bool):
    fraud_log = FraudLog(
        user_id=transaction["user_id"],
        amount=transaction["amount"],
        timestamp=datetime.fromisoformat(transaction["timestamp"]),  # parse string to datetime
        location=transaction["location"],
        is_fraud=is_fraud
    )
    session.add(fraud_log)
    session.commit()