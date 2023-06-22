FROM python:3.9-slim

WORKDIR /app

COPY fibonacci.py .

CMD ["python", "fibonacci.py"]