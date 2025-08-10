from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from app.fraud_detector import detect_fraud
from app.database import create_db_and_tables, SessionLocal
from app.crud import log_transaction

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schemas
class Transaction(BaseModel):
    user_id: str
    amount: float
    timestamp: str
    location: str

class FraudResponse(BaseModel):
    is_fraud: bool
    message: str

# Detect fraud endpoint
@app.post("/detect-fraud", response_model=FraudResponse)
async def detect(transaction: Transaction):
    is_fraud = detect_fraud(transaction.dict())
    message = "Transaction is flagged as fraudulent." if is_fraud else "Transaction is clean."

    # Save transaction to the database
    with SessionLocal() as session:
        log_transaction(session, transaction.dict(), is_fraud)

    return FraudResponse(is_fraud=is_fraud, message=message)

# Serve static files from /static (not root)
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# Create tables on startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()