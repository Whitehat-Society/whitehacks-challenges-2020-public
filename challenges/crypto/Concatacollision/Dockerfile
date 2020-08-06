FROM ubuntu:16.04

# update
RUN apt update

# Setup Server Environment
RUN apt-get install -y \
    python3 \
	python3-pip \
	xinetd

RUN pip3 install pycryptodome

# add new user if it is needed
RUN useradd -d /home/concat/ -m -p concat -s /bin/bash concat

# Change work directory
WORKDIR /home/concat

# Setup the vulnerability environment
COPY concat.py server.py
RUN chmod +x server.py

# xinetd
COPY concat.xinetd /etc/xinetd.d/concat
RUN chmod 444 /etc/xinetd.d/concat
RUN echo "concat                          31337/tcp" >> /etc/services
RUN service xinetd restart

# Entry point
EXPOSE 31337
CMD service xinetd restart && sleep infinity
