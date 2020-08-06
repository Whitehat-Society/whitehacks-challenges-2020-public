FROM i386/ubuntu:xenial
RUN apt-get update
RUN apt-get install -y xinetd build-essential
ENV user=talktome
RUN useradd -m $user
RUN echo "$user     hard    nproc       20" >> /etc/security/limits.conf

COPY ./main.c /home/$user/
COPY ./Makefile /home/$user/
COPY ./service /etc/xinetd.d/$userservice

RUN set -ex \
    && cd /home/$user/ \
    && make

RUN chown -R root:$user /home/$user
RUN chmod -R 750 /home/$user

COPY ./flag.txt /flag
RUN chown root:$user /flag
RUN chmod 440 /flag

USER $user

EXPOSE 1337
ENTRYPOINT ["/usr/sbin/xinetd", "-dontfork"]
