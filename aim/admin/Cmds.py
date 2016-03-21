import json
import urllib.request
def clearMemories(args):
	"""Erase certain or all memories. (/all to wipe memory)"""
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
	"""Find and install memory packages"""
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
		newJson = userJson
		print("Installing new memory...")
		#print("\n")
		for i in package["memories"]:
			print(i)
			if userJson.get(i) != None:
				#print("found same")
				for j in package["memories"][i]:
					#print(j)
					if newJson[i].get(j) != None:
						for k in package["memories"][i][j]:
							#print(k)
							if re.search("," + k + ",",",".join(newJson[i][j])) == None and re.search(",",",".join(newJson[i][j])) != None:
								newJson[i][j].append(k)
							elif re.search(k,",".join(newJson[i][j])) == None:
								newJson[i][j].append(k)
							else:
								pass
					else:
						newJson[i][j] = package["memories"][i][j]
			else:
				newJson[i] = package["memories"][i]
			#print("--------")
		JSON = {
			"memories" : {

			}
		}
		JSON["memories"] = newJson
		finalJson = json.dumps(JSON,indent=4, separators=(',',': '))
		#print("\n\n" + finalJson)
		open("../AI/resources/machine/MachineMemory.json",'w').write(finalJson) 
	pass
