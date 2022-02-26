def students(maths,physics,computerscience):
	sum=maths+physics+computerscience
	if sum>=270:
		print("A+ grade")
	elif sum>=240:
		print("A grade")
	elif sum>=210:
		print("C grade")
	elif sum>=180:
		print("D grade")
	elif sum>=150:
		print("E grade")
	elif sum>=120:
		print("Fgrade")
students(80,80,80)		