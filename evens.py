st1 = ''
for i in range(1000, 3001):
	st1 += (str(i)+',')
st1 = st1[:-1]
ls1 = st1.split(',')

arr = []
for i in ls1:
	c = [j for j in i if not int(j)%2]
	if len(c) == 4:
		arr.append(c)
		
st2 = ''
ls2 = []
for i in range(len(arr)):
	for j in arr[i]:
		st2 += j
	ls2.append(st2)
	
answer = ','.join([ls2[-1][i:i+4] for i in range(0, len(ls2[-1]), 4)])

print(answer)





