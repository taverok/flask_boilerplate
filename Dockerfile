FROM python:3.5-slim

RUN mkdir /counter_app
WORKDIR /counter_app
ADD . .

ENV FLASK_APP=./run.py 

RUN pip install -r requirements.txt

EXPOSE 5000

CMD flask run --host 0.0.0.0
