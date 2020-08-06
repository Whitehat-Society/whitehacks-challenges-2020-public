FROM alpine:3 AS staging

RUN apk add --no-cache npm
COPY package.json /app/package.json

RUN npm --prefix /app install /app

COPY ./public /app/public
COPY ./src /app/src

EXPOSE 3000
RUN npm --prefix /app run build

FROM alpine:3

RUN apk add --no-cache npm
RUN npm install -g serve

COPY --from=staging /app/build /app
EXPOSE 5000

ENTRYPOINT ["serve", "-s", "/app"]