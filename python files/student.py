class Student:
	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno
	
	def intro(self):
		print(f"Hello Everyone..!!,My name is {self.name} and my rollno is {self.rollno}")


	def addition(self,a,b):
		return a+b

s1=Student('Jyoti',34)

s1.intro()
addition=s1.addition(10,12)

print(addition)