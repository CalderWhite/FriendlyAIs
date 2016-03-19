from AI import CmptrMeaning
from Internet.Wiktionary import wiki
from Internet import Yandex
import os
from colorama import init
from colorama import Fore, Back, Style
def line():
	print("────────────────────────────────────────────────────────────────────────────────")
	#print("--------------------------------------------------------------------------------")
	pass;
def reloadMode():
	line()
	mode = input("Please select your mode.\nmode:")
	line()
	return mode;
def gotoMode(Mode):
	running = True
	if Mode == "talk":
		while running:
			UIN = input(":")
			if UIN == "@*$":
				gotoMode(reloadMode())
				running == False
			else:
				CmptrMeaning.processSentance(UIN)
			pass
	elif Mode == "cmd":
		while running:
			CI = input(":").split(" ")
			line()
			if CI[0] == "@*$":
				gotoMode(reloadMode())
				running = False
			elif CI[0] == "getMemories":
				if len(CI) < 2:
					print("Not enough arguments.")
				else:
					CmptrMeaning.memoryBank.printMemories(CI[1])
			else:
				pass
			pass
	elif Mode == "dict":
		while running:
			wordIn = input("word:")
			if wordIn == "@*$":
				gotoMode(reloadMode())
				running = False
			else:
				print("---------------------------------------")
				for i in range(0,len(wiki.words.definition(wordIn))):
					print(wiki.words.definition(wordIn)[i])
					print("---------------------------------------")
				pass;
	elif Mode == "wrdt":
		while running:
			typeIn = input("word:")
			if typeIn == "@*$":
				gotoMode(reloadMode())
				running = False
			else:
				print(Yandex.getWordGram(typeIn))
	elif Mode == "@*$":
		running = False
	else:
		print("unknown mode, please try again.")
		gotoMode(reloadMode())
	pass;
def boot():
	init()
	print(Fore.RED + "WARNING THIS IS OUTDATED, USE A.I.M. in homefolder/aim/aim.py for all commands")
	print(Style.RESET_ALL)
	print("Welcome to my talk line!\nAt the moment I haven't chosen a name, however I will have one soon!")
	line()
	print("\
	 ──────────────────── \n\
	|   Modes:   | Type: |\n\
	|────────────+───────|\n\
	|    Talk    | talk  |\n\
	|────────────+───────|\n\
	|  Command   | cmd   |\n\
	|────────────+───────|\n\
	| Dictionary | dict  |\n\
	|────────────+───────|\n\
	| TypeOfWord | wrdt  |\n\
	 ──────────────────── \n\
		")
	line()
	print("To exit a mode/program at any time type: @*$")
	print("(even this program!)")
	line()
	gotoMode(reloadMode()) 
	pass; 
# finally run the program
boot()