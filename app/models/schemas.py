from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime


# -----------------------------
# Resident Profile
# -----------------------------
from pydantic import BaseModel, Field
from typing import Optional
from datetime import time


class ResidentProfile(BaseModel):
    resident_id: str = Field(..., description="Unique resident identifier")
    age_group: str = Field(..., description="Age category such as 'elderly'")
    fall_risk_level: str = Field(..., description="Risk level: low/medium/high")
    typical_sleep_start: str = Field(..., description="Expected sleep start time, e.g. '22:00'")
    typical_wakeup_time: str = Field(..., description="Expected wake-up time, e.g. '07:00'")
    consent_family_notifications: bool = Field(..., description="Whether family can be notified")
    consent_sensor_monitoring: bool = Field(..., description="Whether sensor monitoring is allowed")



# -----------------------------
# Alert Model
# -----------------------------
class Alert(BaseModel):
    id: str = Field(..., description="Unique alert identifier")
    type: Literal[
        "fall_detected",
        "night_activity",
        "vital_sign_anomaly",
        "emergency_button",
        "environmental_hazard",
    ] = Field(..., description="Type of alert")
    severity: int = Field(..., ge=1, le=5, description="Severity level 1–5")
    timestamp: datetime = Field(..., description="Timestamp of the alert")
    resident_id: Optional[str] = Field(
        None, description="ID of the resident associated with this alert"
    )


# -----------------------------
# Prioritized Alert Output
# -----------------------------
class PrioritizedAlert(BaseModel):
    alert: Alert
    priority_score: float = Field(..., description="Computed priority score")
    reason: str = Field(..., description="Explanation for the prioritization decision")
