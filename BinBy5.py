nums = input('write few 4 digit binary numbers: ').split(',')

ls = []
for i in nums:
	ls.append(int(i, 2))

ls_bin = []
for i in ls:
	if not i%5:
		ls_bin.append(bin(i)[2:])

st = ','.join(ls_bin)
	
print(st)