print('Provide some transactions')

ls = []
while True:
	inp = input()
	if inp:
		ls.append(inp)
	else:
		break
		
balance = 0
for i in ls:
	if i[0] == 'D':
		balance += int(i[2:])
	else:
		balance -= int(i[2:])
	
print(balance)