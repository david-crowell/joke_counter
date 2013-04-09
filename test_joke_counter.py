import joke_counter
from tester import *

def testNoContentMakesNoJokes():
	lines = ["\n"];
	print joke_counter.getJokes(lines)
	return len(joke_counter.getJokes(lines)) == 0

def testNoLineReturnMakesOneJoke():
	lines = ["First joke\n","First joke line 2\n"];
	print joke_counter.getJokes(lines)
	return len(joke_counter.getJokes(lines)) == 1

def testLineReturnMakesTwoJokes():
	lines = ["First joke\n","\n","Second joke\n"];
	print joke_counter.getJokes(lines)
	return len(joke_counter.getJokes(lines)) == 2

def testTwelveJokes():
	lines = ["1\n","\n","2\n","\n","3\n","\n","4\n","\n","5\n","\n","6\n","\n","7\n","\n","8\n","\n","9\n","\n","10\n","\n","11\n","\n","12\n","\n"];
	print joke_counter.getJokes(lines)
	return len(joke_counter.getJokes(lines)) == 12

if __name__ == '__main__':
	runTests(
		[
			Test(testNoContentMakesNoJokes),
			Test(testNoLineReturnMakesOneJoke),
			Test(testLineReturnMakesTwoJokes),
			Test(testTwelveJokes)
		]
		)