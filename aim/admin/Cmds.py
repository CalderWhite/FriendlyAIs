import json
def clearMemories(args):
	name = args[3]
	if name == "/all":
		print("This will reset all of your AI\'s memories, and they are not recoverable.")
		print("Are you sure you want to do this?")
		desicion = input("(Y/N)>")
		desicion = desicion.lower()
		if desicion == "y":
			mem = open("../AI/resources/machine/MachineMemory.json",'r').read()
			sJson = json.loads(mem)
			sJson["memories"] = {}
			strJson = json.dumps(sJson,indent=4, separators=(',',': '))
			open("../AI/resources/machine/MachineMemory.json",'w').write(strJson)
			print("All (machine) memories deleted")
		else:
			print("No memories deleted.")
	else:
		print("Are you sure you want to do this?")
		desicion = input("(Y/N)>")
		desicion = desicion.lower()
		if desicion == "y":
			mem = open("../AI/resources/machine/MachineMemory.json",'r').read()
			sJson = json.loads(mem)
			if sJson["memories"].get(name) != None:
				sJson["memories"].__delitem__(name)
				strJson = json.dumps(sJson,indent=4, separators=(',',': '))
				open("../AI/resources/machine/MachineMemory.json",'w').write(strJson)
			else:
				print("There are no memories for " + name)
		else:
			print("No memories deleted.")