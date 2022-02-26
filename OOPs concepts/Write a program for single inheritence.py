class parent:         # creating a class with parent name
	def __init__(self,name,age): # creating an constructor to  the parent class with two parameters 
		self.name=name   #called instance variables 
		self.age=age
		print("Head of the Family is Dev")
class child(parent):         # creating a class that inherite the parent class
	def __init__(self,name1,age1):
		self.name1=name1
		self.age1=age1

		print( "Which is the class B")
		super().__init__("sand",45)# which is used to calling the super class and passing the arguments to the super class
b=child('sunny',45)   #creating object to the child class with reference object b
print(b.name)
print(b.age)   