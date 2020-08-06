FROM ubuntu:16.04
ENV user bofschool
ENV TERM xterm
ENV COLUMNS 120
ENV LINES 28

# Run Updates
RUN apt-get -y update 
RUN apt-get install -y socat

# Create User
RUN useradd -m $user
WORKDIR /home/$user

# Set Files
COPY bofschool /home/$user
RUN rm -rf /home/$user/.bashrc /home/$user/.profile /home/$user/.bash_logout
RUN ls -al /home/$user

RUN chown -R root /home/$user/
RUN chmod 641 /home
RUN chgrp $user /home/$user/bofschool
RUN chmod 555 /home/$user/bofschool

RUN ls -al /home/$user/

CMD socat TCP-LISTEN:31337,reuseaddr,fork EXEC:/home/bofschool/bofschool
USER $user
EXPOSE 31337
