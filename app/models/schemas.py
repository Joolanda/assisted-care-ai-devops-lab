from pydantic import BaseModel, Field
from datetime import datetime
from typing import List


# -----------------------------
# Resident Profile
# -----------------------------
class ResidentProfile(BaseModel):
    resident_id: str = Field(..., description="Unique resident identifier")
    age_group: str = Field(..., description="Age category such as 'elderly'")
    fall_risk_level: str = Field(..., description="Risk level: low/medium/high")
    typical_sleep_start: str = Field(..., description="Expected sleep start time, e.g. '22:00'")
    typical_wakeup_time: str = Field(..., description="Expected wake-up time, e.g. '07:00'")
    consent_family_notifications: bool = Field(..., description="Whether family can be notified")
    consent_sensor_monitoring: bool = Field(..., description="Whether sensor monitoring is allowed")


# -----------------------------
# Alert Model (matches test suite)
# -----------------------------
class Alert(BaseModel):
    alert_id: str = Field(..., description="Unique alert identifier")
    resident_id: str = Field(..., description="Resident associated with the alert")
    timestamp: datetime = Field(..., description="When the alert occurred")

    severity: str = Field(..., description="Severity level as string: low/medium/high")
    category: str = Field(..., description="Alert category such as environment, fall, etc.")

    message: str = Field(..., description="Human-readable alert message")
    explanation: List[str] = Field(default_factory=list, description="Reasoning or context")
    recommended_action: str = Field(..., description="Suggested next step")
    status: str = Field(..., description="Alert status, e.g. open/closed")


# -----------------------------
# Prioritized Alert Output
# -----------------------------
class PrioritizedAlert(BaseModel):
    alert_id: str
    alert: Alert
    priority_score: float
    reason: str

