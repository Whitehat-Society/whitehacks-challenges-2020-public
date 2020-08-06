FROM ubuntu:16.04

# update
RUN apt update

# Setup Server Environment
RUN apt-get install -y \
    python3 \
	python3-pip \
	xinetd

# add new user if it is needed
RUN useradd -d /home/morale/ -m -p morale -s /bin/bash morale

# Change work directory
WORKDIR /home/morale

# Setup the vulnerability environment
COPY morale.py .
RUN chmod +x morale.py

# xinetd
COPY morale.xinetd /etc/xinetd.d/morale
RUN chmod 444 /etc/xinetd.d/morale
RUN echo "morale                          31337/tcp" >> /etc/services
RUN service xinetd restart

# Entry point
EXPOSE 31337
CMD service xinetd restart && sleep infinity
