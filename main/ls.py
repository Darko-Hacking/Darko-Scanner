# ls.py
# -*- coding: utf-8 -*-
# !/usr/bin/env python

import re, subprocess, threading, socket
from m import *

ip = "192.168.1."

class rechercheHost(threading.Thread):

	def __init__(self, depart, nombre):
		threading.Thread.__init__(self)
		self.depart = depart
		self.nombre = nombre
		rechercheHost.h = 0
		rechercheHost.hosts = []



	def run(self):
		while self.depart <= self.nombre:
			P = subprocess.Popen('ping -c 1 ' + ip + str(self.depart) , stdout = subprocess.PIPE, shell = True)
			out, error = P.communicate()
			out = str(out)
			find = re.search("Destination Host Unreachable", out)
			#find = re.search("0 received", out)
			if find is None:
				rechercheHost.hosts.append(ip + str(self.depart))
				print('[*] hote trouvé')
				rechercheHost.h = rechercheHost.h + 1
			self.depart = self.depart + 1

def start_scan():
	print("----------------------------------------------------------------\n")
	print ("Scan en cours :\n")
	print("----------------------------------------------------------------\n")
	thread_1 = rechercheHost(1, 15)
	thread_2 = rechercheHost(16, 30)
	thread_3 = rechercheHost(31, 45)
	thread_4 = rechercheHost(46, 60)
	thread_5 = rechercheHost(61, 75)
	thread_6 = rechercheHost(76, 100)
	thread_7 = rechercheHost(101, 115)
	thread_8 = rechercheHost(116, 130)
	thread_9 = rechercheHost(131, 145)
	thread_10 = rechercheHost(146, 160)
	thread_11 = rechercheHost(161, 175)
	thread_12 = rechercheHost(176, 200)
	thread_13 = rechercheHost(201, 215)
	thread_14 = rechercheHost(216, 230)
	thread_15 = rechercheHost(231, 254)
	thread_1.start()
	thread_2.start()
	thread_3.start()
	thread_4.start()
	thread_5.start()
	thread_6.start()
	thread_7.start()
	thread_8.start()
	thread_9.start()
	thread_10.start()
	thread_11.start()
	thread_12.start()
	thread_13.start()
	thread_14.start()
	thread_15.start()
	thread_1.join()
	thread_2.join()
	thread_3.join()
	thread_4.join()
	thread_5.join()
	thread_6.join()
	thread_7.join()
	thread_8.join()
	thread_9.join()
	thread_10.join()
	thread_11.join()
	thread_12.join()
	thread_13.join()
	thread_14.join()
	thread_15.join()
	print("\n+-------------------------------------------------+")
	print('|                hote(s) trouvé(s)                |')
	print("+-------------------------------------------------+\n")
	for host in rechercheHost.hosts:
		try:
			name, a, b = socket.gethostbyaddr(host)
		except:
			name = "Nom inconnue"
		print('[*] - ' + host + " - " + name)
	print("\n----------------------------------------------------------------\n")
	print ("Scan Terminé - %d hote(s) trouvé(s)" % rechercheHost.h)
	print('\n----------------------------------------------------------------\n')
	