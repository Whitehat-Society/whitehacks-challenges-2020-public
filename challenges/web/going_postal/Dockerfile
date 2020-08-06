FROM node:8
WORKDIR /usr/src/app
COPY server/. ./

RUN npm install
COPY flag.txt .
EXPOSE 3000

CMD [ "npm", "start" ]