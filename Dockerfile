FROM python:3

WORKDIR /
ADD requirements.txt /
RUN pip install -r requirements.txt