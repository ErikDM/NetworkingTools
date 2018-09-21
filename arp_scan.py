
# Example: sudo arp_scan.py 172.24.3.0/24
import scapy.all as scapy
import sys

try:
	ip = sys.argv[1]
except:
	print("Usage: sudo arp_scan.py LOCAL-IP-RANGE")
	exit()

def scan_network():
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answered = scapy.srp(arp_request_broadcast, timeout=1)[0]
	print("\n ARP response from:\n")
	
	for clients in answered:
		print("[!] IP " + clients[1].psrc)
		print("[!] Mac " + clients[1].hwsrc)
		print("")

scan_network()