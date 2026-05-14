from app.models.schemas import Alert, ResidentProfile, PrioritizedAlert
from datetime import datetime


class AlertPrioritizer:
    def compute_priority(self, alert: Alert, profile: ResidentProfile) -> float:
        score = 0.0

        # Base severity weight
        score += alert.severity * 10

        # Fall risk multiplier
        if profile.fall_risk_level == "high":
            score += 30
        elif profile.fall_risk_level == "medium":
            score += 15

        # Alert type weighting
        if alert.type == "fall_detected":
            score += 100
        elif alert.type == "night_activity":
            score += 20

        # Night‑time boost
        hour = alert.timestamp.hour
        if hour >= 22 or hour < 7:
            score += 10

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
                    reason=f"Computed score {score} based on severity, fall risk, and alert type."
                )
            )

        return sorted(prioritized, key=lambda x: x.priority_score, reverse=True)
