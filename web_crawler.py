# Author: ErikDM
# Date: 18/01-2018
# Recursive web crawler
# Developed for Linux
# Usage: python3 web_crawler.py http://target-ip/ /Path/To/Your/Wordlist.txt

import time, urllib.request, sys

def main():
	print("#####################")
	print("Recursive Web Crawler")
	print("#####################\n")

	try:
		target = sys.argv[1]
		dictionary = sys.argv[2]
	except:
		print("Usage: python3 web_crawler.py http://target-ip/ /Path/To/Your/Wordlist.txt")
		sys.exit()

	print("Starting at:", time.ctime(), "\n")
	start_time = time.time()

	found_directories = ""
	recursive_directories = ""

	try:
		urllib.request.urlopen(target)
	except:
		print("[-] Target is down! Is the URL correct?")
		sys.exit()

	with open("/usr/share/wordlists/metasploit/namelist.txt") as wordlist:
		for i in wordlist:
			fuzz_attack = target + i
			try:
				urllib.request.urlopen(fuzz_attack)
				print("[+] " + fuzz_attack.strip("\n"))
				recursive_directories += (i.strip("\n") + ("\n"))
			except:
				continue
		recursion(wordlist, target, recursive_directories)

		end_time = time.time()
		print("\nTime used:", round(end_time - start_time, 2), "seconds")
		print("Ended at:", time.ctime())

def recursion(wordlist_2, target_2, recursive_directories_2):
	print("\n[!] Starting recursion\n")

	while True:
		recursive_directories_3 = ""
		if recursive_directories_2 == "":
			break

		for a in recursive_directories_2.splitlines():
			wordlist_2.seek(0)
			for b in wordlist_2:
				fuzz_attack_2 = (target_2 + a + "/" + b).strip("\n")
				try:
					urllib.request.urlopen(fuzz_attack_2)
					print("[+] " + fuzz_attack_2.strip("\n"))
					if (a + "/" + b) in recursive_directories_3:
						continue
					else:
						recursive_directories_3 += (a + "/" + b)
				except:
					continue
		recursive_directories_2 = recursive_directories_3

main()
