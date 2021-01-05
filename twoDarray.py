nums = input('Write two integers: ')
X,Y = nums.split(',')
X,Y = int(X),int(Y)

A = [i for i in range(Y)]
B = []

for i in range(X):
	b = [j * i for j in A]
	B.append(b)

print(B)