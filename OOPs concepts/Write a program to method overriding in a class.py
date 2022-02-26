class A:
	def __init__(self):
		print("constructor is working")
	def dev(self,a,b,c): # it will be an method overridden
		d=a+b+c
		return d
		
class B(A):
	def __init__(self):
		print("B class inherited class A")
	def dev(self,a,b,c=0): # it will be an method overriding
		d=a+b+c
		return d
m=B()
print(m.dev(10,20))		