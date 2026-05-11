from datetime import datetime, time
from typing import List, Dict

from app.models.schemas import Alert, ResidentProfile


class AlertPrioritizer:
    """
    Rule-based alert prioritization for assisted living environments.

    Factors:
    - severity
    - resident fall risk
    - night-time boost
    - safety-critical categories
    - alert status (open > acknowledged > resolved)
    - multi-signal support

    This is intentionally explainable and avoids black-box AI.
    """

    SEVERITY_WEIGHTS = {
        "critical": 100,
        "high": 70,
        "medium": 40,
        "low": 10,
    }

    FALL_RISK_WEIGHTS = {
        "high": 40,
        "medium": 20,
        "low": 0,
    }

    STATUS_WEIGHTS = {
        "open": 30,
        "acknowledged": 10,
        "resolved": 0,
    }

    SAFETY_CRITICAL_CATEGORIES = {"emergency", "fall_risk"}

    NIGHT_HOURS = (time(22, 0), time(6, 0))

    def _is_night(self, timestamp: datetime) -> bool:
        t = timestamp.time()
        start, end = self.NIGHT_HOURS
        return t >= start or t <= end

    def prioritize(
        self,
        alerts: List[Alert],
        resident_profiles: Dict[str, ResidentProfile],
    ) -> List[Alert]:
        scored_alerts = []

        for alert in alerts:
            score = 0
            explanations = []

            # Severity
            sev_score = self.SEVERITY_WEIGHTS.get(alert.severity, 0)
            score += sev_score
            explanations.append(f"Severity weight: {sev_score}")

            # Fall risk
            profile = resident_profiles.get(alert.resident_id)
            if profile:
                fall_score = self.FALL_RISK_WEIGHTS.get(profile.fall_risk_level, 0)
                score += fall_score
                explanations.append(f"Fall risk weight: {fall_score}")

            # Night-time boost
            if self._is_night(alert.timestamp):
                score += 15
                explanations.append("Night-time boost: 15")

            # Safety-critical categories
            if alert.category in self.SAFETY_CRITICAL_CATEGORIES:
                score += 25
                explanations.append("Safety-critical category boost: 25")

            # Alert status
            status_score = self.STATUS_WEIGHTS.get(alert.status, 0)
            score += status_score
            explanations.append(f"Status weight: {status_score}")

            # Multi-signal support
            if len(alert.explanation) > 1:
                score += 10
                explanations.append("Multi-signal boost: 10")

            alert.priority_score = score
            alert.explanation.append(f"Priority score: {score}")
            scored_alerts.append(alert)

        return sorted(scored_alerts, key=lambda a: a.priority_score, reverse=True)
