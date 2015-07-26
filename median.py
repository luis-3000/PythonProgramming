"""
median
Great work! You've covered a lot in these exercises. Last but not least, let's write a function to find the median of a list.

The median is the middle number in a sorted sequence of numbers.

Finding the median of [7,12,3,1,6] would first consist of sorting the sequence into [1,3,6,7,12] and then locating the middle value, which would be 6.

If you are given a sequence with an even number of elements, you must average the two elements surrounding the middle.

For example, the median of the sequence [7,3,1,4] is 3.5, since the middle elements after sorting the list are 3 and 4 and (3 + 4) / (2.0) is 3.5.

You can sort the sequence using the sorted() function, like so:

sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]
Instructions
Write a function called median that takes a list as an input and returns the median value of the list.

For example: median([1,1,2]) should return 1.

The list can be of any size and the numbers are not guaranteed to be in any particular order.
If the list contains an even number of elements, your function should return the average of the middle two.

? Hint
In order to find the median of a list with an even number of elements, you're going to need to find the indices of the middle two elements.

You can find the middle two elements by halving the length of the array to find the index of the first element, and subtracting one from the first index to find the second index.

For example, with an array of length 6 like [0,1,2,3,4,5], the two middle elements that need to be averaged in order find the median would be 2 and 3. You get 3 by cutting the length of the array in half and 2 by subtracting 1 from the previous index: 3. You can use a similar pattern to find the middle element of an odd-length list.

Last but not least, note that (2 + 3) / 2 is not the same as (2 + 3) / 2.0! The former is integer division, meaning Python will try to give you an integer back. You'll want a float, so something like (2 + 3) / 2.0 is the way to go.
"""

def median(lst):
	lst.sort()
	result = 0
	length = len(lst)
	middle = length/2
	if length % 2 == 0: # even number of elements in the list
		print "lst[middle]: %s" % (lst[middle])
		print "lst[middle]: %s" % (lst[middle-1])
		result = (lst[middle] + lst[middle-1]) / 2.0
	else:
		result = lst[middle]

	return result

print median([7, 12, 3, 1, 6, 22])


"""

my_list = [7, 12, 3, 1, 6]
my_list.sort();
print my_list # print the sorted list
"""