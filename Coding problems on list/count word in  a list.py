def words(s):
	word=1             # words are always greater than to spaces,thats why here taking word equal to 1,
	for i in s:
		if (i==" "):   
			word=word+1  #counts the each space in a given string and add it into word
	print(word)          # here printing the word it will give total number of words in a string  
words("python is high_level programming language")  