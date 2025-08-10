from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://ashpreetchahal@localhost/fraud_db"
engine = create_engine(DATABASE_URL, echo=True)

# This returns a new session per request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=Session)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)