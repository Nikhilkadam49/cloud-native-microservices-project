from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Visit(BaseModel):
    timestamp: datetime
    ip: str
    user_agent: Optional[str] = "unknown"
    path: Optional[str] = "/"
