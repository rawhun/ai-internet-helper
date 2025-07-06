# Dockerfile for Rasa custom action server
FROM python:3.9-slim

WORKDIR /app

# Install Rasa SDK
RUN pip install rasa-sdk==3.6.2

# Copy actions code
COPY . /app/actions

# Expose port for action server
EXPOSE 5055

# Run the action server
CMD ["rasa", "run", "actions", "--port", "5055", "--actions", "actions"] 