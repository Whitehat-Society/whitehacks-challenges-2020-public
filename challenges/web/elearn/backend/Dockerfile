FROM alpine:3

RUN apk add --no-cache python3 py3-pip py3-mysqlclient
COPY requirements.txt /app/requirements.txt
RUN pip3 --no-cache-dir install -r /app/requirements.txt

COPY . /app

ENV FLASK_APP /app/app
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_SQLALCHEMY_DATABASE_URI mysql://whitehacks:whitehacks@db/whitehacks
ENV FLASK_SECRET_KEY WHITEHACKS
EXPOSE 5000

ENTRYPOINT ["flask", "run"]