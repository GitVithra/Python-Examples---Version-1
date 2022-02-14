def function():
	yield 1
	yield 2
	yield 6
for i in function():
	print(i)