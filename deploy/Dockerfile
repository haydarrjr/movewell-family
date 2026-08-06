# Movewell Family Multi-Service Container
FROM python:3.11-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY movewell_engine/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY movewell_engine/ /app/movewell_engine/

EXPOSE 8000 2091

CMD ["uvicorn", "movewell_engine.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
