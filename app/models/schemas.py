from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime


# -----------------------------
# Resident Profile
# -----------------------------
class ResidentProfile(BaseModel):
    id: str = Field(..., description="Unique resident identifier")
    name: Optional[str] = Field(None, description="Resident full name")
    fall_risk: int = Field(..., ge=0, le=10, description="Fall risk score from 0–10")
    mobility_level: Literal["low", "medium", "high"] = Field(
        ..., description="Resident mobility classification"
    )
    cognitive_state: Literal["normal", "impaired", "critical"] = Field(
        ..., description="Cognitive state relevant for alert prioritization"
    )


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
