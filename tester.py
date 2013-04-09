class Test:
	def __init__(self, test = None, name = ''):
		self.name = name
		self.test = test
		self.passed = None	

	def __call__(self):
		return self.test()

	def __str__(self):
		return str(self.name) + " : " + str(self.test)

def runTests(tests):
	passed = []
	failed = []
	for test in tests:
		passes = test()
		test.passed = passes
		if (passes):
			passed.append(test)
		else:
			failed.append(test)

	print "\n#### SUCCESSES ####"

	for test in passed:
		print test

	print "\n#### FAILURES ####"

	for test in failed:
		print test

	print ''

	print "\n#### SUMMARY ####"		
	print len(passed), " SUCCESSES"
	if len(failed):
		print len(failed), " FAILURES"
	print "#################\n"