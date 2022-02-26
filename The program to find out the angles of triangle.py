def triangle(a,b,c):
	if (a==b and b==c):
		print("is equilateral")
	elif (a==b or b==c or c==a):
		print("is isoscele")
	elif (a!=b and b!=c and c!=a):
		print("this is scalene")
triangle(10,10,10)				