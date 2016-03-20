import json
import urllib.request
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
def get(args):
	u = args[3]
	print("Finding Package...")
	tree = urllib.request.urlopen("https://api.github.com/repos/FriendlyAIs/aim-Packages/forks").read().decode('utf-8')
	tjson = json.loads(tree)
	repo = None
	for i in tjson:
		if u.lower() == i["name"].lower():
			repo = i
	if repo == None:
		print("There is no package " + u)
	else:
		print("Retrieving package...")
		source = repo["url"]
		newUrl = source.replace("https://api.github.com/repos","https://raw.githubusercontent.com")
		newUrl = newUrl + "/Friendly-Ai-memos-Json/MachineMemory.json"
		content = urllib.request.urlopen(newUrl).read().decode('utf-8')
		rJson = json.loads(content)
		package = rJson
		userMemories = open("../AI/resources/machine/MachineMemory.json",'r').read()
		userJson = json.loads(userMemories)["memories"]
		print("Installing new memory...")
		for i in package:
			if userJson.get(i) != None:
				for j in package[i]:
					if userJson[i].get(j) != None:
						for k in j:
							userJson[i][j].append(package[i][j][k])
					else:
						userJson[i][j] = package[i][j][k]
			else:
				userJson[i] = {}
				for j in package[i]:
					userJson[i][j] = package[i][j]
		JSON = {
			"memories" : {

			}
		}
		JSON["memories"] = userJson["memories"]
		finalJson = json.dumps(JSON,indent=4, separators=(',',': '))
		open("../AI/resources/machine/MachineMemory.json",'w').write(finalJson) 
	pass
