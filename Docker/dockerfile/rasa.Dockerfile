FROM python:3.7

RUN pip3 install rasa==1.10.10 --no-cache-dir

RUN pip3 install spacy

RUN python3 -m spacy download en_core_web_md

RUN python3 -m spacy link en_core_web_md en

RUN pip3 install mysql-connector-python

RUN apt-get update

RUN apt-get install -y supervisor

WORKDIR /app

COPY Docker/bin/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY config.yml /app/config.yml
COPY domain.yml /app/domain.yml

RUN sed -i 's/MinProtocol = TLSv1.2/MinProtocol = TLSv1.0/' /etc/ssl/openssl.cnf

RUN rasa train

CMD ["/bin/bash", "Docker/bin/rasa_run.sh"]
