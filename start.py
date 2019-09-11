#!/usr/bin/python
import os


os.system("command")
print("Registry install")
#domain = raw_input("Type domain address: ")
#user = raw_input("Type username: ")
#password = raw_input("Type password: ")
#email = raw_input("Type email for ssl: ")
dir1 = "/etc/letsencrypt/live/"
dir2 = "/crtdata/"
#cmd_line = "certbot certonly --standalone --preferred-challenges http --non-interactive  --staple-ocsp --agree-tos -m " + email + " -d " + domain
path_auth = "./genpass/auth.txt"
path_command = "./certs/command_file.txt"


if os.path.exists(path_auth):
	print("Start install........................")
else:
	domain = raw_input("Type domain address: ")
	user = raw_input("Type username: ")
	password = raw_input("Type password: ")
	email = raw_input("Type email for ssl: ")
	cmd_line = "certbot certonly --standalone --preferred-challenges http --non-interactive  --staple-ocsp --agree-tos -m " + email + " -d " + domain
	print("Data: " + user + ":" + password + "@" + domain)
	print("Email: " + email)
	auth_file = open('./genpass/auth.txt','w')
	auth_data = "htpasswd -Bbn " + user + " " + password + " > passfile"
	auth_file.write(str(auth_data))
	auth_file.close()
	#############################################
	certs_file = open('./certs/command_file.txt','w')
	certs_data = str(	cmd_line + "\n" 
			"cd " + dir1 + domain + "\n"
			"cp ./privkey.pem ./domain.key \n"
			"cat ./cert.pem ./chain.pem > ./domain.crt \n"
			"cp -r "+ dir1 + domain + " " + dir2 + "\n")
	certs_file.write(certs_data)
	certs_file.close()


os.system("chmod -R 777 ./genpass/")
os.system("chmod -R 777 ./certs/")
os.system("chmod -R 777 ./letsencrypt11/")

os.system("docker-compose -f ./docker-compose-First.yml build")
os.system("docker-compose -f ./docker-compose-First.yml up")
os.system("docker rm $(docker ps -a -f status=exited -q)")
os.system("docker-compose -f ./docker-compose-Main.yml build")
os.system("docker-compose -f ./docker-compose-Main.yml up")
