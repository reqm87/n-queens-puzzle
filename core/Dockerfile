FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /queenspuzzle
WORKDIR /queenspuzzle
COPY requirements.txt /queenspuzzle/
RUN pip install -r requirements.txt
COPY . /queenspuzzle/

