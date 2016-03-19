import sys
import commands
import aim
import os
import re
import admin
args = sys.argv[1:]
def getCmds():
	cmds = []
	for method in dir(commands):
		if callable(getattr(commands, method)) and str(method)[0:1] != "_":
			cmds.append(method)
	return cmds;
def searchCmds(arg):
	ret = False
	for i in getCmds():
		if i == arg:
			ret = True
	return ret;
if __name__ == '__main__':
	#unstable version:
	#Test if a passwrd has already been set
	if admin.outside.check():
		#with open("aim.py",'w') as myfile:
		wrd = input("Input Your PERMANENT password.\nWrite this down!.\n>")
		File = open("aim.py","r").read()
		admin.outside.wrt(File,wrd)
	else:
		pass
	if len(args) == 0:
		print("Usage:\n    aim <command> [input]\nFor more help use:\n    aim help")
	elif searchCmds(args[0]):
		if len(args) == 1:
			commands.__getattribute__(args[0]).__call__()
		elif len(args) > 1:
			os.system("title aim - " + args[0])
			commands.__getattribute__(args[0]).__call__(args)
			os.system("title " + os.getcwd())
	elif args[0] == "/admin":
		if args[1] == "password":
			pass
			if args[2] == "RESET":
				admin.outside.reset()
				pass
			else:
				if len(args) < 4:
					print("herro")
				else:
					admin.Cmds.__getattribute__(args[2]).__call__(args)
		else:
			print("Wrong Password")
			exit()
			os.system('exit')
	else:
		print("No command such as [" + args[0] + "] Type: aim help for all comands.")
