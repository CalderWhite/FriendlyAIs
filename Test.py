import re
from Wiktionary import wiki
import Yandex
theVerb = "plays"
for i in wiki.words.findAllDefs(theVerb):
	for j in i:
		if re.search("third-person",j) != None:
			jArray = j.split(" ")
			if Yandex.findType(Yandex.getWordGram(jArray[len(jArray) - 1]),"verb"):
				Stype = "declarationVerb"