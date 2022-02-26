def fact(x):   #program to find factorial number by using function 
	if x==0:
		return 1
	return x*fact(x-1) # findig factorial of number by using formula to the factorial is n(n-1)(n-2)..1 
print(fact(5))		

import math        # we can find factorial number by using math madule
def factorial(n):
	return(math.factorial(n))
print(factorial(5))
