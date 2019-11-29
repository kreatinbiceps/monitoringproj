#Projekt = Monitoring
import os
import time
import subprocess
from ping3 import ping, verbose_ping
from colorama import Fore, Back, Style

#öppna hostfilen
f = open('hostlist.txt', 'r')
hostname = f.readlines()

#infinite while loop för att låta pingen gå
a = 1
while a == 1:

	for x in range(len(hostname)): 		#går igenom varje variabel i arrayen hostlist.txt

		response = ping(hostname[x].rstrip(), timeout=0.5)

		#print (response)
		if response == None:
			print (Back.RED + hostname[x].rstrip(), 'is down!' + Style.RESET_ALL)

		else:
			print (hostname[x].rstrip(), 'is up!')

	f.close()
	print("\nNext ping in 10 seconds\n")
	time.sleep(10)
