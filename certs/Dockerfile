FROM centos:latest
RUN yum install epel-release -y
RUN yum install certbot -y
CMD mkdir crtdata && mkdir /data
WORKDIR /data
ADD cmd.txt /data
CMD chmod +x cmd.txt
#EXPOSE 80
#EXPOSE 443
#ENTRYPOINT ["/bin/bash"]
CMD /data/cmd.txt
#CMD ["/data/cmd.txt"]
