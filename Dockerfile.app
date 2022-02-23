FROM python:3.8-slim

COPY ./app /app
COPY ./requirements.txt / 
COPY ./wait-for-it.sh /

ENV PYTHONPATH="/:$PYTHONPATH"

RUN apt-get -y update &&\
    apt-get -y install \
    apt-utils \
    libpq-dev \
    postgresql-common \
    postgresql-client \
    gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r /requirements.txt