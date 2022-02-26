def palindrome(num):      # palindrome means that reads the number,which is equal to it's reverse of the number
	temp=num
	reverse=0
	while num>0:
		digit=num%10      # it gives the remainder of the digit
		reverse=reverse*10+digit # add the digit of the number to reverse*10
		num=num//10      # it check the condtion untill num//10  is zero means loop will be terminated
	if(temp==reverse):
		print("number is palindrome")
	else:
		print("number is not a palindrome")
palindrome(1331)		#it is palindrome number