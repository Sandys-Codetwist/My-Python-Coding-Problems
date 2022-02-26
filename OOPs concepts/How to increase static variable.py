class Test:
	x=10 # A variable which is inside a class is called static variable 
	def test(self,y):
		self.y=y
		return y 	
print(Test.x)	
Test.x=Test.x+1 #here we increasing static variable
print(Test.x)

t=Test()
print(t.test(20))