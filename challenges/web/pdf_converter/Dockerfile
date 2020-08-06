FROM node:12
WORKDIR /usr/src/app

RUN echo "node     hard    nproc       20" >> /etc/security/limits.conf

RUN apt-get update
RUN apt-get install -y xinetd build-essential
RUN apt-get install -y tesseract-ocr
RUN apt-get install -y imagemagick --fix-missing
RUN apt-get install -y ghostscript
RUN apt-get install -y poppler-utils

COPY server/ ./
RUN chmod -R 555 .
RUN chmod 477 uploads

RUN npm install

COPY ./getinfo.c /getinfo.c
RUN gcc /getinfo.c -o /getinfo
RUN chmod u+s /getinfo
RUN rm /getinfo.c

COPY info.txt /info.txt
RUN chown -R root:root /info.txt
RUN chown -R root:root /info.txt
RUN chmod -R 400 /info.txt

COPY ./flag1.txt flag1.txt
RUN chown root:node flag1.txt
RUN chmod 440 flag1.txt

COPY ./flag2.txt flag2.txt
RUN chown root:node flag2.txt
RUN chmod 440 flag2.txt

EXPOSE 8080

USER node
CMD ["npm", "start" ]