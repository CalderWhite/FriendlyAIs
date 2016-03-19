from random import random
greetings = ["hi","hello","salutations","Kon'nichiwa","hey","sup","what's popin\'?","good day","howdy","greetings, earthling"]
def prin(phrase):
	print("BOT>>" + phrase)
def greeting():
	return greetings[int(random() * 10)];