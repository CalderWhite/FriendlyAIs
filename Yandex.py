import json
import urllib.request
import re
import sys
import socket
try:
	source = urllib.request.urlopen("http://google.com")
except urllib.error.URLError:
        print("The internet must be turned on for this library to work")
def getWordGram(search):
	source = urllib.request.urlopen("https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20160314T163727Z.61245f4bffecefda.edfa4501171fe3ecf04efe7cbe89428833593ec7&lang=en-en&text=" + search).read()
	# I request a translate from english to russian, though I don't need it. The data I need is already in the returned json
	# (is it a noun,article,verb,interjection etc.)
	source = source.decode('utf-8')
	sJson = json.loads(source)
	rArray = []
	for i in range(0,len(sJson["def"])):
		rArray.append(sJson["def"][i]["pos"])
	if rArray == []:
		rArray = ["noun"]
	return rArray
def findAllTypes(array,toBeSearched):
	for i in array:
		if i == toBeSearched:
			return True;
		if re.search(toBeSearched,i) != None:
			# If it's a 'proNOUN' it's still a 'noun'
			# If it was to be exclusive, it would be named 'findType'
			return True; 
def findType(array,toBeSearched):
	for i in array:
		if i == toBeSearched:
			return True 
