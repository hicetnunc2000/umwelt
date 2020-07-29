# Docker Image which is used as foundation to create
# a custom Docker Image with this Dockerfile
FROM node:latest

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app

RUN npm install
COPY . /usr/src/app

EXPOSE 3000
CMD ["npm","start"]