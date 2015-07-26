 phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
    if char == 'A' or char == 'a':
        print 'X' , #trailing comma = print on same line
    else:
        print char ,
#Don't delete this print statement!
print

# Looping over a dictionary
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    print key + " " + d[key]

"""
Counting as you go
A weakness of using this for-each style of iteration is that you don't 
know the index of the thing you're looking at. Generally this isn't an
issue, but at times it is useful to know how far into the list you are.
 Thankfully the built-in enumerate function helps with this.

enumerate works by supplying a corresponding index to each element in
the list that you pass it. Each time you go through the loop, index
will be one greater, and item will be the next item in the sequence. 
It's very similar to using a normal for loop with a list, except this 
gives us an easy way to count how many items we've seen so far.
"""    
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index+1, item

"""
Multiple lists
It's also common to need to iterate over two lists at once. This is 
where the built-in zip function comes in handy.
zip will create pairs of elements when passed two lists, and will stop
at the end of the shorter list.

zip can handle three or more lists as well!
"""    
# compare which element is bigger, then print it

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    if a > b:
        print a
    else:
        print b
"""
For / else
Just like with while, for loops may have an else associated with them.

In this case, the else statement is executed after the for, but only if
the for ends normally—that is, not with a break. This code will break
when it hits 'tomato', so the else block won't be executed.

Instructions
Click Save & Submit Code to see how for and else work together.
"""        
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'


