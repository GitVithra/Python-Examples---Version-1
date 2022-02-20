class Student:
	# constructor
	def __init__(self,name,age):
		#instance variable
		self.name = name
		self.age = age
# create object

s = Student("pavithra",21)

# use getattar instead of s.name

print("Name:", getattr(s,'name'))
print("Age:", getattr(s,'age'))