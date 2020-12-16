class TwoMethods:
	def getString(self):
		st = input('Write something: ')
		return st
	def printString(self, getString):
		return print(getString.upper())
		
def trial(test):
	test.printString(test.getString())
	return print('Bravo!')
	
experiment = TwoMethods()

trial(experiment)