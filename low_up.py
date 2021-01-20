sen = input('Say something: ')

upper, lower = 0, 0

for i in sen:
	if 'a' <= i <= 'z':
		lower += 1
	if 'A' <= i <= 'Z':
		upper += 1
		
print(f'lower case {lower}\nupper case {upper}')
