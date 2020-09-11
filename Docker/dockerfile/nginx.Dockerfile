FROM nginx:1.19.1-alpine

RUN apk add --no-cache bash

WORKDIR /app

COPY ./Docker/nginx.conf /etc/nginx/nginx.conf

CMD ["/bin/bash", "-c", "Docker/env.sh && nginx -g \"daemon off;\""]
