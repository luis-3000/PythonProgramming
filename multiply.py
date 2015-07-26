"""
product
Great! Now let's try a little multiplication.

Instructions
Define a function called product that takes a list of integers as input and returns the product of all of the elements in the list.

For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).

Don't worry about the list being empty.
Your function should return an integer.
"""

def product(lst):
	multiplied = 1
	for i in range(len(lst)):
		multiplied *= lst[i]

	return multiplied

print product([1, 2, 3, 4, 5, 6])			