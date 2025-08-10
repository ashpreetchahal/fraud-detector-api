# Fraud Detector API

A fast, reliable fraud detection system built with FastAPI and PostgreSQL.  
It flags suspicious transactions based on multiple rules including large amounts, transaction spikes, and blacklisted locations.

## Features

- Real-time fraud detection via REST API  
- Persistent transaction logging to PostgreSQL  
- Simple, extensible rules engine  
- Clean, well-documented code for easy maintenance

## Tech Stack

- FastAPI  
- SQLModel & SQLAlchemy  
- PostgreSQL  
- Python 3.11+

## Usage

1. Clone the repo  
2. Create and activate a virtual environment  
3. Install dependencies with `pip install -r requirements.txt`  
4. Configure your PostgreSQL database in `app/database.py`  
5. Run the app with:  
   ```bash
   uvicorn app.main:app --reload
6. Access the API docs at http://127.0.0.1:8000/docs

## API Endpoints
GET / - Check if API is running
POST /detect-fraud - Submit a transaction for fraud check

Example Request:
{
  "user_id": "user123",
  "amount": 15000,
  "timestamp": "2025-08-10T10:00:00",
  "location": "RU"
}

## License
MIT License © Ashpreet Chahal
