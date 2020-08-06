FROM node:8
WORKDIR /usr/src/app
COPY server/ ./
RUN chmod -R 555 .

RUN echo "node     hard    nproc       20" >> /etc/security/limits.conf

RUN apt-get update
RUN apt-get install -y xinetd build-essential

RUN npm install

COPY ./readflag.c /readflag.c
RUN gcc /readflag.c -o /readflag
RUN chmod u+s /readflag
RUN rm /readflag.c

COPY flag.txt /flag.txt
RUN chown -R root:root /flag.txt
RUN chown -R root:root /flag.txt
RUN chmod -R 400 /flag.txt

EXPOSE 8080

USER node
CMD ["npm", "start" ]