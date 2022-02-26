class A:
	def __init__(self,x1,x2):   #creating a constructor to class A 
		self.x1=x1              #instance variables
		self.x2=x2
		print("constructor is working")# printing string statement
	def add(self):           #instance method
		c=10+20
		return c
	def sub(self):           # a class having multiple methods and by using "self" keyword we can...s 
		c=20-10              #   access the attributes and methods of the class
		return c
a=A(23,36)
print(a.add())
print(a.sub())	
			