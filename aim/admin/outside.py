import re
def wrt(UI,wrds):
	open("aim.py",'w').write(UI.replace("== KEYPASSWRD","== \"" + wrds + "\""))
	pass
def reset():
	wrd = "== \"" + input("Enter Your Password >") + "\""
	thisFile = open("aim.py",'r').read()
	print(thisFile)
	open("aim.py",'w').write(thisFile.replace(wrd,"== KEYPASSWRD"))
	pass
def check():
	if re.search("== KEYPASSWRD",open("aim.py",'r').read()) != None:
		return True;
	else:
		return False; 