FROM alpine:3

RUN apk add --no-cache python3 py3-setuptools py3-flask py3-lxml

COPY app.py /app/app.py
COPY flag.txt /app/flag.txt

ENV FLASK_APP /app/app
ENV FLASK_RUN_HOST 0.0.0.0
EXPOSE 5000

ENTRYPOINT ["flask", "run"]