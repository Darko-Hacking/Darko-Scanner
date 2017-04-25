# isc.py
# -*- coding: utf-8 -*-
# !/usr/bin/env python

import socket, re
from m import *

ouverts = 0

def start_scan_ip():
	print("----------------------------------------------------------------\n")
	host = raw_input("Veuillez renseignez l'ip a scanner ou l'adresse web [ ex : xxx.xxx.xxx.xxx ou votresite.com ] \n>> ") # On demande le hôte (plus lisible)
	print("\n----------------------------------------------------------------\n")
	ouverts = 0
	 
	ports = {21: "ftp", 22: "SSH", 23: "telnet", 25: "smtp", 69: "tftp", 80: "http", 110: "pop3", 115: "sftp", 119: "nntp", 123: "ntp", 135: "loc-srv", 139: "netbios", 143: "imap", 194: "irc", 443:"https", 445: "microsoft-ds", 465: "smtp/ssl", 554: "rtsp", 563: "nntp", 587: "msm", 993: "imap/ssl", 995: "pop3/ssl", 2869: "ics/icf", 5357: "webservices", 8080: "http-cache", 10000: "ndmp"}

	print("Scan en cours :\n")
	print("----------------------------------------------------------------\n")
	 
	for port in xrange(1, 65536):
	    try:
	        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	        s.settimeout(0.05) # Scan très rapide mais pas forcément fiable
	                            # si la connexion a un ping pourri
	        s.connect((host, port))
	        if port in ports:
	            print("[*] - Port n°%d (%s) ouvert" % (port, ports[port]))
	        else:
	            print("[*] - Port n°%d ouvert" % port)
	        ouverts += 1
	    except socket.error as err:
	        pass # Ne rien faire en cas d'erreur		     

	print("\n----------------------------------------------------------------\n")
	print("Scan Terminé - %d port(s) ouvert(s)" % ouverts)
	prin("\n----------------------------------------------------------------\n")