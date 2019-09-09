FROM centos:latest
RUN yum install epel-release -y
RUN yum install certbot -y
CMD mkdir crtdata && mkdir /data
WORKDIR /data
ADD cmd.txt /data
CMD chmod +x cmd.txt
CMD /data/command_file.txt
