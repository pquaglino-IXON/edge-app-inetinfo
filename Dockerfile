# Use the official lightweight Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install system dependencies required for cryptography
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libssl-dev \
        libffi-dev \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY inetinfo.py .
EXPOSE 50080
CMD ["python", "inetinfo.py"]