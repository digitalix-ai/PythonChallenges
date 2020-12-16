class TwoMethods:
	def getString(self):
		self.st = input('Write something: ')

	def printString(self):
		print(self.st.upper())
		
def trial(test):
	test.getString()
	test.printString()
	
experiment = TwoMethods()

trial(experiment)
