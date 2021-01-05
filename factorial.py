get_input = int(input("\n Write a whole number greater than 0: "))

a = []  # List to hold the multiplication steps
base = 1

for multiplier in range(1, get_input + 1):
	base *= multiplier
	a.append(base)
	
	
print(f'\n Factorial of {get_input} is {a[-1]}. \n')