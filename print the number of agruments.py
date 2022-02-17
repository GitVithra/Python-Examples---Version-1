def multiply(*args):
	mult = 2
	for number in args:
		mult = mult*number
		return mult
print(multiply(1,2,3,5))

