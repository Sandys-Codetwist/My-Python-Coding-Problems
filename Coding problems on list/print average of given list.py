def averagelist(l):
	total=0
	for ele in range(0,len(l)):
		total=total+len(l)
		avg=total/len(l)
	return avg
print(averagelist([1,2,3,4,5,6,7,8,9]))	


l=[1,2,3,4,5,6,7,8,9]
l1=sum(l)
avg=l1/len(l)
print(avg)
print(l1)