def spliting(string):
	for each in string:
		if each==',':   #here check the condition is each equal to ','
			pass        # here nothing to be printed in place of ','
		else:
			print(each,end=" ")
s="pyhton,django,flask,Data science"	
spliting(s)		