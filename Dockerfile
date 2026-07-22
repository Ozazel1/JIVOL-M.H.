FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY jivol.py .
COPY .env.example .

RUN mkdir -p backups output logs

ENV PORT=8080
ENV PYTHONUNBUFFERED=1
ENV BACKUP_ENABLED=true
ENV BACKUP_INTERVAL=3600
ENV MAX_BACKUPS=10
ENV LOG_LEVEL=INFO

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "4", "--timeout", "120", "jivol:app"]
