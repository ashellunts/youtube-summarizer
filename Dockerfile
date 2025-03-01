FROM python:3.10.7 AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
WORKDIR /app


RUN python -m venv .venv
COPY requirements.txt ./
RUN .venv/bin/pip install -r requirements.txt
FROM python:3.10.7-slim
WORKDIR /app
COPY --from=builder /app/.venv .venv/
COPY src ./src
COPY templates ./templates
COPY static ./static
COPY server.py ./
CMD ["/app/.venv/bin/python", "server.py"]