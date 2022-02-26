l=[]
for i in range(500,1000):
	if (i%7==0) and (i%5!=0): # here using logical operater for cheking two conditions and "and" operater return true when two conditions are true
		l.append(i)           # here appended each element to the list
print(l)                      #printing l		
