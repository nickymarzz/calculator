# Dockerfile
FROM python:3.9-slim-buster
WORKDIR /app
COPY calculator.py .
CMD ["python", "calculator.py"]