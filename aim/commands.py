import commands
import os
import json
import sys
sys.path.append(os.getcwd() + "../Internet/HTTPFunctions.py")
from HTTPFunctions import *
import urllib.request
def help():
    """return a list of aim commands"""
    def repDif(str2,str1,rep):
        """To make all the content apear in columns"""
        dif = len(str2) - len(str1)
        nS = str1
        for i in range(0,dif):
            nS = nS + rep
        return nS;
    cmds = []
    for method in dir(commands):
        if callable(getattr(commands, method)) and str(method)[0:1] != "_":
            cmds.append(method)
    print("A.I.M. Command List:")
    print("--------------------")
    for i in cmds:
        print(repDif("------------",str(i).upper()," ") + "    " + commands.__getattribute__(i).__getattribute__("__doc__").upper())
    print("\n There is no furthur information on this project yet,\n\
 since the github repository is private.\n\
 However, there will be more details when the project goes public.")
    pass; 
def memories(entity):
	"""print an entity's memories /all to print all memories"""
	grabbedMemos = open("../AI/resources/machine/MachineMemory.json").read()
	memoJSON = json.loads(grabbedMemos)
	# I'm lazy, okay?
	if entity[1].lower() == "/all":
		print("A.I.M. memory recall:\n---------------------")
		print("memories")
		memos = memoJSON["memories"]
		for i in memos:
			if list(memos.keys()).index(i) != len(list(memos.keys())) - 1:
				print("   ├────" + str(i) + ":")
				for j in memos[i]:
					if list(memos[i].keys()).index(j) != len(list(memos[i].keys())) - 1:
						print("   │       ├───┬" + str(j) + ":")
					else:
						print("   │       └───┬" + str(j) + ":")
					for k in memos[i][j]:
						if memos[i][j].index(k) != len(memos[i][j]) - 1:
							if list(memos[i].keys()).index(j) != len(list(memos[i].keys())) - 1:
								print("   │       │   ├" + str(i) + " " + str(j).lower() + " " + str(k))
							else:
								print("   │           ├" + str(i) + " " + str(j).lower() + " " + str(k))
						else:
							if list(memos[i].keys()).index(j) != len(list(memos[i].keys())) - 1:
								print("   │       │   └" + str(i) + " " + str(j).lower() + " " + str(k))
							else:
								print("   │           └" + str(i) + " " + str(j).lower() + " " + str(k))
			else:
				print("   └────" + str(i) + ":")
				for j in memos[i]:
					if list(memos[i].keys()).index(j) != len(list(memos[i].keys())) - 1:
						print("           ├───┬" + str(j) + ":")
					else:
						print("           └───┬" + str(j) + ":")
					for k in memos[i][j]:
						if memos[i][j].index(k) != len(memos[i][j]) - 1:
							if list(memos[i].keys()).index(j) != len(list(memos[i].keys())) - 1:
								print("           │   ├" + str(i) + " " + str(j).lower() + " " + str(k))
							else:
								print("               ├" + str(i) + " " + str(j).lower() + " " + str(k))
						else:
							if list(memos[i].keys()).index(j) != len(list(memos[i].keys())) - 1:
								print("           │   └" + str(i) + " " + str(j).lower() + " " + str(k))
							else:
								print("               └" + str(i) + " " + str(j).lower() + " " + str(k))
	else:
		memos = memoJSON["memories"]
		if memos.get(entity[1]) != None:
			print("A.I.M. memory recall:\n---------------------")
			i = entity[1].lower()
			print(str(i) + ":")
			for j in memos[i]:
				if list(memos[i].keys()).index(j) != len(list(memos[i].keys())) - 1:
					print("   ├───┬" + str(j) + ":")
				else:
					print("   └───┬" + str(j) + ":")
				for k in memos[i][j]:
					if memos[i][j].index(k) != len(memos[i][j]) - 1:
						if list(memos[i].keys()).index(j) != len(list(memos[i].keys())) - 1:
							print("   │   ├" + str(i) + " " + str(j).lower() + " " + str(k))
						else:
							print("       ├" + str(i) + " " + str(j).lower() + " " + str(k))
					else:
						if list(memos[i].keys()).index(j) != len(list(memos[i].keys())) - 1:
							print("   │   └" + str(i) + " " + str(j).lower() + " " + str(k))
						else:
							print("       └" + str(i) + " " + str(j).lower() + " " + str(k))
		else:
			print("There are no memories for " + entity[1])
	pass;
	