FROM centos:latest
#EXPOSE 443 80
RUN yum install epel-release -y
RUN yum install certbot -y
CMD mkdir /crtdata && mkdir /data
WORKDIR /data
ADD command_file.txt /data
CMD chmod +x command_file.txt
CMD /data/command_file.txt
