FROM ubuntu:16.04


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev libmysqlclient-dev 

WORKDIR /app

COPY app/ /app/

RUN pip install -r requirements.txt

CMD [ "python", "./server.py" ]
