#Projekt = Monitoring // Hostlista

a = 1


while a == 1:
	userInput = int(input("Press 1 to add host. Press 2 to show list. Press 3 to quit\n"))
	if userInput == 1:
		saveFile = open('hostlist.txt', 'a')
		hostlist = input('Add a host to the monitoring list: ')
		saveFile.write(hostlist + "\n")
		saveFile.close()

	elif userInput == 2:
		showFile = open('hostlist.txt', 'r').read()
		print(showFile)
	elif userInput == 3:
		break



