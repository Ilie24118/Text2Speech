# Pull base image
FROM python:3.10-slim

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libasound2-dev \
    libpq-dev \
    libcairo2-dev \
    libgirepository1.0-dev \
    pkg-config \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /code/django_project

# Install dependencies
COPY ./requirements.txt /code/django_project
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install wheel
RUN pip install unrealspeech
RUN pip install playsound
RUN pip install pydub
RUN pip install simpleaudio
RUN pip install pycairo
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/
