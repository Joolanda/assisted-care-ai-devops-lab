from fastapi import FastAPI

APP_NAME = "Assisted Care AI DevOps Lab"
APP_VERSION = "0.1.0"

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=(
        "A portfolio MVP demonstrating AI DevOps practices for responsible, "
        "privacy-aware assisted-care workflows."
    ),
)

@app.get("/")
def root() -> dict[str, str]:
    return {
        "service": APP_NAME,
        "version": APP_VERSION,
        "message": "Welcome to the Assisted Care AI DevOps Lab.",
    }

@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": APP_NAME,
        "version": APP_VERSION,
    }

@app.get("/metrics")
def metrics() -> dict[str, int | str]:
    return {
        "service_status": "ok",
        "requests_total": 0,
        "sensor_events_received": 0,
        "alerts_generated": 0,
        "rag_queries_total": 0,
    }