FROM python:3.8-buster

# update
RUN apt update

# Setup Server Environment
RUN apt-get install -y xinetd

RUN pip3 install pycryptodome Faker sympy

# add new user if it is needed
RUN useradd -d /home/waifu/ -m -p waifu -s /bin/bash waifu

# Change work directory
WORKDIR /home/waifu

# Setup the vulnerability environment
COPY server.py .
RUN chmod +x server.py

# xinetd
COPY waifu.xinetd /etc/xinetd.d/waifu
RUN chmod 444 /etc/xinetd.d/waifu
RUN echo "waifu                          31337/tcp" >> /etc/services
RUN service xinetd restart

# Entry point
EXPOSE 31337
CMD service xinetd restart && sleep infinity
