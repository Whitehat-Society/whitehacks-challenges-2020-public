FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install xinetd -y

WORKDIR /home/gdbtutor
RUN chmod 555 .
RUN chmod 555 /home

RUN useradd -ms /bin/bash gdbtutor
COPY dist/gdbtutor.xinetd /etc/xinetd.d/gdbtutor
RUN chmod 444 /etc/xinetd.d/gdbtutor
RUN echo "gdbtutor                          31337/tcp" >> /etc/services

COPY dist /home/gdbtutor
RUN chmod 444 /home/gdbtutor/flag.txt
RUN chmod 444 /home/gdbtutor/geedeebee
RUN chmod 555 /home/gdbtutor/crackme.c
RUN chmod 555 /home/gdbtutor/crackme.bin
RUN chmod 555 /home/gdbtutor/gdb
RUN chmod 555 /home/gdbtutor/run.sh

RUN service xinetd restart

RUN chown -R root:root .

EXPOSE 31337

ENV COLUMNS 130
CMD service xinetd restart && sleep infinity
