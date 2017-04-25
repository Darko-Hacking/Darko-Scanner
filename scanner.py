#!/usr/bin/env python
# -*- coding: utf-8 -*-
from main.isc import *
from main.ls import *
from main.m import *

try:
	print("\033c")
	print(" ______________________________________________________________")
	print("|                                                              |")
	print("|                                                              |")	
	print("|          ██████╗  █████╗ ██████╗ ██╗  ██╗ ██████╗            |")
	print("|          ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔═══██╗           |")
	print("|          ██║  ██║███████║██████╔╝█████╔╝ ██║   ██║           |")
	print("|          ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██║   ██║           |")
	print("|          ██████╔╝██║  ██║██║  ██║██║  ██╗╚██████╔╝           |")
	print("|          ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝            |")
	print("|                                                              |")
	print("| ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗  |")
	print("| ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗ |")
	print("| ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝ |")
	print("| ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗ |")
	print("| ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║ |")
	print("| ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ |")
	print("|                                                         v1.0 |")
	print("|______________________________________________________________|")
	print('                                                            ')
	print('                                                            ')
	print('[+] Choisissez : ')
	print('[1] - Scanner réseau local')
	print("[2] - Scanner port")
	print("[3] - fermer")
	print('                                                            ')
	print('----------------------------------------------------------------')
	print('                                                            ')
	choice = raw_input('Veuillez entrer votre choix >> ')
	print('                                                            ')
	x = 1

	if int(choice) == 1:
		
		start_scan()
		quit_app()

	elif int(choice) == 2:
		
		start_scan_ip()
		quit_app()

	elif int(choice) == 3:
		quit_1()

	else:
		execl("scanner.py", "")

	print('')

except KeyboardInterrupt:
	quit()
except EOFError:
	quit()