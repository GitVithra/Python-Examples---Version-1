class Student:
	# Parameterised Constructor 
	def __init__(self,name,age):
		self.name = name
		self.age = age
	# create method
	def display(self):
		print("Name:{} \n Age:{}".format(self.name,self.age))
		print("Name:%s \n Age:%d" %(self.name,self.age))
# calling the object with the help of refference variable
s1 = Student("Pavithra",21)
s1.display()

