

def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False    

"""
is_int
An integer is just a number without a decimal part (for instance, -17, 0, and 42 are all integers, but 98.6 is not).

For the purpose of this lesson, we'll also say that a number with a decimal part that is all 0s is also an integer, such as 7.0.

This means that, for this lesson, you can't just test the input to see if it's of type int.

If the difference between a number and that same number rounded down is greater than zero, what does that say about that particular number?

Instructions
Define a function is_int that takes a number x as an input.
Have it return True if the number is an integer (as defined above) and False otherwise.
For example:

is_int(7.0)   # True
is_int(7.5)   # False
is_int(-1)    # True      
"""
from math import floor

def is_int(x):
    if (x - floor(x)) > 0:
        return False
    else:
        return True

print is_int(7.0) # True
print is_int(7.5) # False
print is_int(-1) # True        

""""
digit_sum
Awesome! Now let's try something a little trickier. Try summing the
digits of a number.

Instructions
Write a function called digit_sum that takes a positive integer n as 
input and returns the sum of all that number's digits.

For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4.

(Assume that the number you are given will always be positive.)

Check the hint if you need help!

Hint
One way might be to convert the integer to a string with str(), divide
 it up, and turn the substrings back into integers with int() to do the
 addition.

If you're looking for a challenge, try this: to get the rightmost digit
of a number, you can modulo (%) the number by 10. To remove the 
rightmost digit you can floor divide (//) the number by 10. (Don't 
worry if you're not familiar with floor division. You can look up 
the documentation here. Remember, this is a challenge!)

Try working this into a pattern to isolate all of the digits and add
them to a total.
""" 

# Takes a positive integer n and returns the sum of all the 
# number's digits
def digit_sum(n):
    sum = 0
    n = abs(n)
    while n >= 1:
        sum += n % 10 # get the rightmost digit
        n = n // 10 # then, remove it with a 'floor divide' (//) by 10
        
    return sum

print "digit_sum(1234): %s" % (digit_sum(1234))


"""
factorial
All right! Now we're cooking. Let's try a factorial problem.

To calculate the factorial of a non-negative integer x, just multiply
 all the integers from 1 through x. For example:

factorial(4) would equal 4 * 3 * 2 * 1, which is 24.
factorial(1) would equal 1.
factorial(3) would equal 3 * 2 * 1, which is 6.
Instructions
Define a function factorial that takes an integer x as input.

Calculate and return the factorial of that number.
"""
def factorial(x):
    if x <=1:
        return 1
    else:
        return x * factorial(x-1)


"""
is_prime
A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself. (Boy, that's a mouthful.)

In other words, if you want to test if a number in a variable x is prime, then no other number should go into x evenly besides 1 and x. So 2 and 5 and 11 are all prime, but 4 and 18 and 21 are not.

If there is a number between 1 and x that goes in evenly, then x is not prime.

Instructions
Define a function called is_prime that takes a number x as input.
For each number n from 2 to x - 1, test if x is evenly divisible by n.
If it is, return False.
If none of them are, then return True.
"""        
def is_prime(x):
    if x < 2:
        return False
    prime_flag = True
    for i in range(2,x):
        if x % i == 0:
            prime_flag = False
            break
    return prime_flag

print "is_prime(-2): %s") % (is_prime(-2))
print "is_prime(3): %s") % (is_prime(3))
print "is_prime(5): %s") % (is_prime(5))
print "is_prime(20): %s") % (is_prime(20))


"""
reverse
Great work so far! Let's practice writing some functions that work with
strings.

Instructions
Define a function called reverse that takes a string textand returns
that string in reverse.

For example: reverse("abcd") should return "dcba".

You may not use reversed or [::-1] to help you with this.
You may get a string containing special characters (for example, !, @,
or #).

HINT:
Consider how you would loop through text starting from the last
 character through the first character.
"""
#Using iteration
def reverse(text):
    return ''.join([text[i] for i in xrange(len(text)-1, -1, -1)])

#Using recursion
def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]   	

#OR if allowed to use [::1]    	
'STRING'[::1]


def anti_vowel(text):
    result = ""
    for c in text:
        if c not in "aeiouAEIOU":
            result += c
    
    return result

    