FROM nginx:stable

RUN apt-get update \
    && apt-get install -y cron bash wget certbot \
    && apt-get update -y \
    && mkdir -p /webroots /scripts \
    && rm -f /etc/nginx/conf.d/default.conf

WORKDIR /app

COPY ./Docker/ /app/Docker/

COPY ./certibot/ /scripts/

COPY ./Chatbot-Widget/ /usr/share/nginx/html/

RUN chmod +x /scripts/*.sh

#VOLUME /etc/letsencrypt

COPY ./Docker/bin/nginx.conf /etc/nginx/nginx.conf

RUN echo "22 03 * * 2,7 root /scripts/renew.sh" >/etc/cron.d/certbot-renew

CMD ["sh", "-c", "cron && Docker/env/env.sh && nginx -g 'daemon off;'"]
