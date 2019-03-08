FROM python:3.4.2

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y memcached
RUN apt-get install -y libmemcached-dev
RUN service memcached start
RUN pip install splinter

RUN mkdir /app
ADD cr4ck.py /app
ADD user_list.txt /app

WORKDIR /app
