
n = [3, 5, 7]

def total(numbers):
    result = 0
    #for i in range(len(list)):
    #    print list(i)
    for i in range(len(numbers)):
        result += numbers[i]
        
    return result  

"""
Using two lists as two arguments in a function
Using multiple lists in a function is no different from just using multiple arguments in a function!

a = [1, 2, 3]
b = [4, 5, 6]
print a + b
# prints [1, 2, 3, 4, 5, 6]
The example above is just a reminder of how to concatenate two lists.

Instructions
Create a function that joins two lists together.

On line 4, define a function called join_lists that has two arguments, x and y. They will both be lists.
Inside that function, return the result of concatenating x and y together.
"""    
m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x, y):
    return x + y

print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]

"""
Using a list of lists in a function
Finally, this exercise shows how to make use of a single list that contains multiple lists and how to use them in a function.

		list_of_lists = [[1,2,3], [4,5,6]]

		for lst in list_of_lists:
		    for item in lst:
		        print item

In the example above, we first create a list containing two items, each of which is a list of numbers.
Then, we iterate through our outer list.
For each of the two inner lists (as lst), we iterate through the numbers (as item) and print them out.
We end up printing out:

1
2
3
4
5
6

Instructions
Create a function called flatten that takes a single list and concatenates all the sublists that are part of it into a single list.

01. On line 3, define a function called flatten with one argument called lists.
02. Make a new, empty list called results.
03. Iterate through lists. Call the looping variable numbers.
04. Iterate through numbers.
05. For each number, .append() it to results.
06. Finally, return results from your function.
"""
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    for numbers in lists:
        for item in numbers:
            results.append(item)
    
    return results

print flatten(n)

"""

"""