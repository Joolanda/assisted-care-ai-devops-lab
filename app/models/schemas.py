from pydantic import BaseModel
from typing import Optional

class Alert(BaseModel):
    id: str
    type: str
    severity: int
    timestamp: str
    resident_id: Optional[str] = None

class ResidentProfile(BaseModel):
    id: str
    fall_risk: int
    mobility_level: int
    cognitive_state: str
