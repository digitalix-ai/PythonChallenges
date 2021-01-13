no_of_lines = int(input('How many lines will you provide? '))

lines = ''

for i in range(no_of_lines):
	lines += input('Write a line: ') + '\n'
	
print('\n'+lines.upper())