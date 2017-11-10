FROM python:2.7

ENV PYTHONUNBUFFERED=1

RUN pip install splinter

RUN mkdir /app
ADD cr4ck.py /app
ADD user_list.txt /app

WORKDIR /app
CMD python cr4ck.py
