class A:
	def __init__(self):
		
		print("It is an A class")
	def dev(self):          # instance method
		return " dev is the method in side the class A"	
class B:
	def __init__(self):
	
		print( "Which is the class B")
	def  enjoy(self):
		return "enjoy is the method in side the class B"
class C:                      
	def __init__(self):
		
		print("Which is class c")
class D(C,B,A):                 # one class that inherite multiple  base classes called multiple inheritence  
	def __init__(self,x4):
		self.x4=x4
		print("Which is class c that inherite class b")
	
b=D(49)
print(b.dev())
print(b.enjoy())		



