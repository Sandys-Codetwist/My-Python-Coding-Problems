class A:
	def __init__(self):
		
		print("It is an A class")
	def dev(self):          # instance method
		return " dev is the method which is inside the class A"	
class B(A):             # creating class B that inherite class A
	def __init__(self):
	
		print( "Which is the class B")
	def  enjoy(self):
		return "enjoy is the method which is inside the class B"
class C(B):        # creating aclass C that inherite the derived class B called multileve inheritence              
	def __init__(self):
		
		print("Which is class c")

b=C()
print(b.dev())
print(b.enjoy())		



