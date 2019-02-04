FROM python:3.6.8-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /project
WORKDIR /project
COPY . /project/
RUN pip install -Ur requirements.txt
