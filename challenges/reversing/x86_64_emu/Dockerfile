FROM ubuntu:16.04

# update
RUN apt update

# Setup Server Environment
RUN apt-get install -y \
    python \
    socat \
	python-pip \
	xinetd

RUN pip install --no-cache-dir pwntools unicorn termcolor

# add new user if it is needed
RUN useradd -d /home/emu/ -m -p emu -s /bin/bash emu

# Change work directory
WORKDIR /home/emu

# Setup the vulnerability environment
COPY server.py .
RUN chmod +x server.py
COPY run.sh .
RUN chmod +x run.sh

# xinetd
COPY emu.xinetd /etc/xinetd.d/emu
RUN chmod 444 /etc/xinetd.d/emu
RUN echo "emu                          31337/tcp" >> /etc/services
RUN service xinetd restart

# Entry point
EXPOSE 31337
CMD service xinetd restart && sleep infinity
