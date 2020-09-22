FROM python:3.7

RUN apt-get update

RUN pip3 install mysql-connector-python

RUN pip install flask-restful

RUN apt-get install -y vim

EXPOSE 3000

WORKDIR /app

COPY ./responses.py /app

COPY ./database_connector.py /app

RUN sed -i 's/MinProtocol = TLSv1.2/MinProtocol = TLSv1.0/' /etc/ssl/openssl.cnf

CMD ["python", "responses.py"]
