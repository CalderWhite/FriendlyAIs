from AI import CmptrMeaning
from random import random
# To see how it processes large data.
# (It does well! (in recalling it almost instantly. Input needs work))
verbs = ["plays","is","has","makes"]
for i in range(20):
	for j in verbs:
		print("Current sentance " + str(random()) + " " + j + " " +  str(i))
		print("---------------------------------")
		CmptrMeaning.processSentance(str(random()) + " " + j +  " " +  str(i))