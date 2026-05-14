import json
from pathlib import Path
from app.models.schemas import ResidentProfile

def load_resident_profiles() -> dict[str, ResidentProfile]:
    path = Path("app/data/residents.json")
    data = json.loads(path.read_text())
    return {rid: ResidentProfile(**profile) for rid, profile in data.items()}
