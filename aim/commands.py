import commands
import os
import json
import sys
import admin.Cmds
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
    adminCommands = []
    for method in dir(admin.Cmds):
        if callable(getattr(admin.Cmds, method)) and str(method)[0:1] != "_":
            adminCommands.append(method)
    print("A.I.M. Command List:")
    print("--------------------")
    for i in cmds:
        print(repDif("------------------",str(i).upper()," ") + "    " + commands.__getattribute__(i).__getattribute__("__doc__").upper())
    print("--------------------")
    print("ADMIN COMMANDS:")
    print("--------------------")
    for i in adminCommands:
    	print(repDif("------------------",str(i).upper()," ") + "    " + admin.Cmds.__getattribute__(i).__getattribute__("__doc__").upper())
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
	
def listPackages():
	class fork(object):
		def __init__(self,repoName,html_url,owner):
			self.name = repoName
			self.url = html_url
			self.owner = owner
			pass
	source = urllib.request.urlopen("https://api.github.com/repos/FriendlyAIs/aim-Packages/forks").read().decode('utf-8')
	ob = json.loads(source)
	#print(ob)
	forks = []
	for i in ob:
		forks.append(fork(
			i["name"],
			i["html_url"],
			i["owner"]["login"]
			))
	print("AIM Packages")
	print("-------------")
	for i in forks:
		print("Package Name : " + i.name)
		print(i.url)
		print("Owned by: " + i.owner)
		print("-------------")
	pass