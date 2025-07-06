# Dockerfile for Rasa server with health check
FROM python:3.9-slim

WORKDIR /app

# Install Rasa and FastAPI
RUN pip install rasa==3.6.2 fastapi uvicorn

# Copy Rasa project files
COPY . /app

# Railway uses PORT environment variable
ENV PORT=5005

# Expose Rasa and health check ports
EXPOSE $PORT 8000

# Start both Rasa server and health check
CMD ["sh", "-c", "rasa run --enable-api --cors '*' --port $PORT & uvicorn health:app --host 0.0.0.0 --port 8000"] 