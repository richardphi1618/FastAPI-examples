FROM python:3.8
LABEL version="1.0"

RUN pip install --upgrade pip
COPY ./api/src /code/app

RUN pip install --no-cache-dir -r /code/app/requirements.txt

WORKDIR /code/app



