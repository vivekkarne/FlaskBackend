# pull official base image
FROM python:3.6.13-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install requirements
RUN pip3 install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt

# copy src app
COPY . /usr/src/app/