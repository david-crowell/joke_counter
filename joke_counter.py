import os
import string as string

JOKE_FILENAME = 'jokes.txt'

class Joke:	
	def __init__(self, text):
		self.text = text
		self.number = -1	
	
	def getText(self):
		return self.text

	def setText(self, text):
		self.text = text

	def addText(self, newText):
		self.text += newText

	def getNumber(self):
		return self.number

	def setNumber(self, number):
		self.number = number

	def __str__(self):
		return str((self.number, self.text))

	def __repr__(self):
		return self.__str__()

def getJokes(lines):
	jokes = []
	joke = None
	for line in lines:
		if all(c in string.whitespace for c in line):
			if joke != None:
				jokes.append(joke)
				joke = None
			continue 

		if (joke == None):
			joke = Joke(line)
		else:
			joke.addText(line)
	if joke != None:
				jokes.append(joke)
				joke = None
	return jokes

def getLines(filename):
	file = open(filename)
	lines = file.readlines()
	file.close()
	return lines

def getCountFromFilename(filename):
	lines = getLines(filename)
	jokes = getJokes(lines)
	return len(jokes)

if __name__ == '__main__':
	print getCountFromFilename(JOKE_FILENAME)

