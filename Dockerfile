FROM python:3.11-slim AS base

# ---------------------------------------------------------
# 1. System setup
# ---------------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------------------------------------
# 2. Install Python dependencies
# ---------------------------------------------------------
COPY pyproject.toml .

RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir fastapi "uvicorn[standard]" pydantic \
    && pip install --no-cache-dir pytest httpx ruff

# ---------------------------------------------------------
# 3. Copy application code
# ---------------------------------------------------------
COPY . .

# ---------------------------------------------------------
# 4. Security: run as non-root user
# ---------------------------------------------------------
RUN useradd -m appuser
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
