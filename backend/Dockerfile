FROM python:3.11-slim

WORKDIR /code

# Define PYTHONPATH para resolver imports
ENV PYTHONPATH=/code/src

# Instala dependências de sistema para o Postgres e para o OpenCV (GUI/Render)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libxcb1 \
    libglvnd0 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .