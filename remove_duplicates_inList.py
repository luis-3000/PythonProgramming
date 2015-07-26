"""
remove_duplicates
Awesome! Now for something a bit trickier.

Instructions
Write a function remove_duplicates that takes in a list and removes elements of the list that are the
 same.

For example: remove_duplicates([1,1,2,2]) 
should return [1,2].

Don't remove every occurrence, since you need to keep a single occurrence of a number.
The order in which you present your output does not matter. So returning [1,2,3] is the same as
 returning [3,1,2].
Do not modify the list you take as input! Instead, return a new list.

? Hint
The easiest way to approach this problem is to create a new list in your function, loop through your
 input list, and add items from your input list to your new list if the current item is not already 
 contained in your new list. Using the 'a' not in 'b' syntax might help you here.

Also, note that destructively modifying a list while you are looping through it is bad practice and
 will likely lead to bugs somewhere down the line! That's why we always make a fresh copy to work on.
"""

def remove_duplicates(lst):
	result = []
	for i in range(len(lst)):
		if lst[i] not in result:
			result.append(lst[i])

	return result			

print remove_duplicates([1, 2, 3, 1, 4, 1, 2, 3, 4])