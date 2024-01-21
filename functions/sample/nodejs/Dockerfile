FROM node:18.12.1-bullseye-slim

RUN npm install -g npm@9.1.3

ADD package.json .
ADD server.js .


RUN npm install

EXPOSE 3000

CMD [ "npm", "start" ]
