def amstrong(num):     #amstrong means sum of n'th digits of it's power
	sum=0
	temp=num
	while temp>0:
		digit=temp%10    #it gives the remainder of the digit
		sum=sum+digit**3 # if we want to 3 digits of amstrong number
		temp//=10        # it check the while condtion to be zero it means loop will be terminate    
	if num==sum:
		print(num,"is amstrong number")
	else:
		print(num,"is not a amstrong")
amstrong(153)
