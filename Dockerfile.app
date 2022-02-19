FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app
COPY ./requirements.txt / 

ENV PYTHONPATH="/:$PYTHONPATH"

RUN pip install -r /requirements.txt