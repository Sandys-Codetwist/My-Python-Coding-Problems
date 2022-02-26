def palindrome(value):  # it reads the value which is equal to reverse of the same value
	if value==value[::-1]: # condition to the palindrome number
		print("the value is palindrome")
	else:
		print("value is not a palindrome")
palindrome("1441")
