FROM nginx:1.19.1-alpine

RUN apk add --no-cache bash

WORKDIR /app

COPY ./Docker/bin/nginx.conf /etc/nginx/nginx.conf

CMD ["/bin/bash", "-c", "Docker/env/env.sh && nginx -g \"daemon off;\""]
