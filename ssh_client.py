# A fully interactive python based SSH client
# Author: ErikDM
# Date: 04/01-2018

import paramiko, sys, getpass

print("######################\nSSH Client Application\n######################\n")
hostname = input("Server IP: ")
username = input("Username: ")
password = getpass.getpass()

try:
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
	client.connect(hostname, username=username, password=password)
	print("\n[+] Connected!")
except:
	print("[-] Failed to connect")
	sys.exit()

print("Type 'exit' to abort the connection")
while True:
	command = input("Shell $: ")
	if command == ("exit"):
		break
	if command == ("Exit"):
		break
	if command == ("EXIT"):
		break

	stdin, stdout, stderr = client.exec_command(command)
	stdin.close()
	answer = (repr(stdout.read()))
	print(answer[2:-3])

stdout.close()
stderr.close()
client.close()
print("[-] Connection closed")
