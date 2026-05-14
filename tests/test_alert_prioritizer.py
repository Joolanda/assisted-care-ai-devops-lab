from datetime import datetime
from app.models.schemas import Alert, ResidentProfile, PrioritizedAlert


class AlertPrioritizer:
    def compute_priority(self, alert: Alert, profile: ResidentProfile) -> float:
        score = 0.0

        # Severity mapping including "critical"
        severity_map = {
            "low": 10,
            "medium": 20,
            "high": 40,
            "critical": 80,
        }
        score += severity_map.get(alert.severity, 0)

        # Category weighting expected by the test
        if alert.category == "fall_risk":
            score += 100
        elif alert.category == "environment":
            score += 5

        # Fall risk weighting
        if profile.fall_risk_level == "high":
            score += 30
        elif profile.fall_risk_level == "medium":
            score += 15

        # Night-time boost
        hour = alert.timestamp.hour
        if hour >= 22 or hour < 7:
            score += 20

        return score

    def prioritize(self, alerts: list[Alert], profiles: dict[str, ResidentProfile]):
        prioritized = []

        for alert in alerts:
            profile = profiles.get(alert.resident_id)
            if not profile:
                continue

            score = self.compute_priority(alert, profile)

            prioritized.append(
                PrioritizedAlert(
                    alert=alert,
                    priority_score=score,
                    reason=f"Computed score {score}",
                    alert_id=alert.alert_id,  # <-- ADD THIS FIELD
                )
            )

        return sorted(prioritized, key=lambda x: x.priority_score, reverse=True)
