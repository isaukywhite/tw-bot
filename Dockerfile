
FROM python:3.12.4-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update --fix-missing && apt-get install -y \
    gcc libc6-i386 && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
COPY ./src .
CMD ["python", "app.py"]
