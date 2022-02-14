class Animal:
	x=10
	def eat(self):#instance method
		self.x=10 # instance variable
		return " Hlo...."
	def food():#static method
		x = 20
		return " Hi "
Animal()
a = Animal()
print(a.eat())
print(a.x)
print(Animal.food())
print(a.x)