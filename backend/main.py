from fastapi import FastAPI
from pydantic import BaseModel
import datetime

app = FastAPI()

class LogEntry(BaseModel):
    user_id: str
    event_type: str  # e.g., login, data_access, file_download
    timestamp: datetime.datetime
    ip_address: str
    data_size: float  # MB transferred
    location: str  # Based on IP
@app.post("/log_event/")
async def log_event(event: LogEntry):
    # Save event to DB
    return {"message": "Event logged successfully"}

@app.get("/alerts/")
async def get_alerts():
    # Retrieve anomaly alerts
    return {"alerts": ["Unusual login detected"]}
