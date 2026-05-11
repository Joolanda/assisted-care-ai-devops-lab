from datetime import datetime

from app.services.alert_prioritizer import AlertPrioritizer
from app.models.schemas import Alert, ResidentProfile


def test_alert_prioritization_orders_correctly():
    prioritizer = AlertPrioritizer()

    profiles = {
        "r1": ResidentProfile(
            resident_id="r1",
            age_group="elderly",
            fall_risk_level="high",
            typical_sleep_start="22:00",
            typical_wakeup_time="07:00",
            consent_family_notifications=True,
            consent_sensor_monitoring=True,
        )
    }

    alert_low = Alert(
        alert_id="a1",
        resident_id="r1",
        timestamp=datetime(2024, 1, 1, 14, 0),
        severity="low",
        category="environment",
        message="Temp slightly high",
        explanation=[],
        recommended_action="Check room",
        status="open",
    )

    alert_critical = Alert(
        alert_id="a2",
        resident_id="r1",
        timestamp=datetime(2024, 1, 1, 2, 0),
        severity="critical",
        category="fall_risk",
        message="Night-time bed exit with no motion",
        explanation=["bed_exit", "no_motion"],
        recommended_action="Check resident immediately",
        status="open",
    )

    prioritized = prioritizer.prioritize([alert_low, alert_critical], profiles)

    assert prioritized[0].alert_id == "a2"
    assert prioritized[1].alert_id == "a1"
