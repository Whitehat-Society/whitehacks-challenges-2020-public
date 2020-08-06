FROM ubuntu:18.04

RUN apt-get update && apt-get install -y openssh-server && apt-get install git -y
RUN mkdir /var/run/sshd
RUN useradd -c "Chris Wang" -m chrisw
RUN echo "chrisw:7cj5dvv4uhBRLIpMNPeT" | chpasswd

RUN mkdir /home/chrisw/.aws
COPY credentials /home/chrisw/.aws
RUN mkdir /shell
COPY custom_shell /shell
RUN chmod 777 /shell/custom_shell

# SSH login fix. Otherwise user is kicked off after login   
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

RUN usermod -s /shell/custom_shell chrisw

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]