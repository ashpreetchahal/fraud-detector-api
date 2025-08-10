from datetime import datetime, timedelta
from typing import List, Dict

recent_transactions: Dict[str, List[datetime]] = {}

def rule_large_amount(amount: float, threshold: float = 10000) -> bool:
    return amount > threshold

def rule_transaction_spike(user_id: str, timestamp: datetime, window_minutes: int = 1, max_transactions: int = 3) -> bool:
    now = timestamp
    user_transactions = recent_transactions.get(user_id, [])
    user_transactions = [t for t in user_transactions if now - t < timedelta(minutes=window_minutes)]

    if len(user_transactions) >= max_transactions:
        return True

    user_transactions.append(now)
    recent_transactions[user_id] = user_transactions
    return False

def rule_suspicious_location(location: str, blacklist: List[str] = None) -> bool:
    if blacklist is None:
        blacklist = {"NG", "RU", "CN"}
    return location in blacklist

def detect_fraud(transaction: dict) -> bool:
    amount = transaction.get("amount", 0)
    user_id = transaction.get("user_id")
    timestamp_str = transaction.get("timestamp")
    location = transaction.get("location", "unknown")

    if not timestamp_str:
        return False

    try:
        timestamp = datetime.fromisoformat(timestamp_str)
    except ValueError:
        return False

    if rule_large_amount(amount):
        return True

    if user_id and rule_transaction_spike(user_id, timestamp):
        return True

    if rule_suspicious_location(location):
        return True

    return False