FROM python:3.8

LABEL version="1.0"

COPY ./api/app.py ./
RUN pip install --upgrade pip
COPY ./api/requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt
