# Dockerfile for retrain pipeline
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
RUN pip install transformers torch sqlalchemy psycopg2-binary pyyaml

# Copy retrain pipeline code
COPY . /app

CMD ["python", "retrain.py"] 