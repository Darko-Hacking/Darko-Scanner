# m.py
# -*- coding: utf-8 -*-
# !/usr/bin/env python
import os, sys, string, subprocess

def taille():
	P = subprocess.Popen('stty size' , stdout = subprocess.PIPE, shell = True)
	out, error = P.communicate()
	out = str(out)
	width = string.split(out, " ")
	return int(width[1])

def quit_app():
	quit = raw_input("Voulez vous quitter Darko Scanner [Y/n] >> ")
	if str(quit) == "n":
		execfile("scanner.py")
		sys.exit()
	elif str(quit) == "y":
		print("\n----------------------------------------------------------------\n")
		print("              Darko Scanner © copyright 2017 v1.0               ")
		print("\n----------------------------------------------------------------\n")
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)

def quit():
	print("\n\n----------------------------------------------------------------\n")
	print("              Darko Scanner © copyright 2017 v1.0               ")
	print("\n----------------------------------------------------------------\n")
	try:
		sys.exit(0)
	except SystemExit:
		os._exit(0)

def quit_1():
	print("----------------------------------------------------------------\n")
	print("              Darko Scanner © copyright 2017 v1.0               ")
	print("\n----------------------------------------------------------------\n")
	try:
		sys.exit(0)
	except SystemExit:
		os._exit(0)