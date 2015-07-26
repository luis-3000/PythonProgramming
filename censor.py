"""
censor
You're doing great with these string function challenges. Last one!

Instructions
Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks.

For example:

censor("this hack is wack hack", "hack") 
should return

"this **** is wack ****"
01. Assume your input strings won't contain punctuation or upper case letters.

02. Assume your input strings won't contain punctuation or upper case letters.
The number of asterisks you put should correspond to the number of letters in the censored word.
?
Hint
You can use

string.split()

# and 
" ".join(list)
to help you here.

Remember:
"*" * 4 equals "****"


After splitting the string with string.split(), you can loop through the indices in the list and replace the words you are looking for with their asterisk equivalent. Join the list at the end to get your sentence!

"""
def censor(text, word):
	wordlist = text.split() # split into individual words. Gives a list of words from string
	print wordlist
	result = [] #list to store each of our words
	final_result = ''
	for c_word in range(len(wordlist)):  #get each individual word from the string
		print "c_word: %s" % (wordlist[c_word])
		if wordlist[c_word] == word:
			result.append("*" * len(word))
			print "result %s" % (result)
		else:
			result.append(wordlist[c_word])
			print "result %s" % (result)

	final_result = " ".join(result)
	print "final_result %s" % (final_result)
	return final_result

censor("this hack is wack hack", "hack")