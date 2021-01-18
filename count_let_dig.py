import re

st = input('write: ')

ren = re.findall(r'\d*', st)
rel = re.findall(r'[a-zA-Z]*', st)

nums=''
for i in ren:
	if len(i)>0:
		nums += i
		
lets=''
for i in rel:
	if len(i)>0:
		lets += i

print(f'letters: {len(lets)}')
print(f'digits: {len(nums)}')