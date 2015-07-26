count = 0

if count < 5:
    print "Hello, I am an if statement and count is", count
    
while count <= 9:
    print "Hello, I am a while and count is", count
    count += 1

loop_condition =  True
while loop_condition:
	print "I am a loop"
	loop_condition = False

num = 1
while num <= 10:  # Fill in the condition
    # Print num squared
    print num **2
    # Increment num (make sure to do this!)
    num += 1

choice = raw_input('Enjoying the course? (y/n)')
while ((choice != "y") and (choice != "n")):  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")    

#infinite loop fixed
count = 0
while count < 10: # Added a colon (syntax error)
    print count
    # Increment count (logic error fixed)
    count += 1    

# Break statement to exit out of a loop
count = 0
while True:
    print count
    count += 1
    if count >= 10:
        break    
"""
While / else
Something completely different about Python is the while/else 
construction. while/else is similar to if/else, but there is a 
difference: the else block will execute anytime the loop condition
 is evaluated to False. This means that it will execute if the loop
  is never entered or if the loop exits normally. If the loop exits 
  as the result of a break, the else will not be executed.

In this example, the loop will break if a 5 is generated, and the else
will not execute. Otherwise, after 3 numbers are generated, the loop 
condition will become false and the else will execute.        
"""
import random
print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"
count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"

""" Allow a user to guess what the number is three time """
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
            #need int(X) to make X a number again
    guess = int(raw_input("Your guess: ")) 
    if guess == random_number:
        print 'Your win!'
        break
    guesses_left -= 1
else:
    print 'You lose.' 


print "Counting..."
# This means, "for each number i in the range 0 to 9"
for i in range(10):
    print i    


hobbies = []
# Add your code below!
for i in range(3):
    hobby = raw_input("Please tell me 3 of your hobbies? ")
    hobbies.append(hobby)   
print hobbies     