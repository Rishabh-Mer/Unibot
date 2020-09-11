FROM node:alpine
RUN npm install -g json-server
EXPOSE 3000
WORKDIR /app
CMD ["json-server", "--host", "0.0.0.0", "data/data.json"]
