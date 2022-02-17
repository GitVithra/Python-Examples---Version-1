def my_bottle(**kwargs):
	for key,value in kwargs.items():
		print('{}:{}'.format(key,value))
my_bottle(color = "yellow",name="zirpy",capacity=2,height = 10)