"""
Why Use Classes?
Python is an object-oriented programming language, which means it manipulates programming constructs called objects. You can think of an object as a single data structure that contains data as well as functions; functions of objects are called methods. For example, any time you call

len("Eric")
Python is checking to see whether the string object you passed it has a length, and if it does, it returns the value associated with that attribute. When you call

my_dict.items()
Python checks to see if my_dict has an items() method (which all dictionaries have) and executes that method if it finds it.

But what makes "Eric" a string and my_dict a dictionary? The fact that they're instances of the str and dict classes, respectively. A class is just a way of organizing and producing objects with similar attributes and methods.


"""

class Fruit(object): #class Class_Name (class_name from which Class_Name inherits some behavior/attributes)
    """A class that makes various tasty fruits."""


    """ Constructor """
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

"""
--------------
Instructions |
--------------
Check out the code in the editor above. We've defined our own class, Fruit, and created a lemon 
instance.

When you're ready, click Save & Submit Code to get started creating classes and objects of your own.

"""


"""
Classier Classes
We'd like our classes to do more than... well, nothing, so we'll have to replace our pass with 
something else.

You may have noticed in our example back in the first exercise that we started our class definition 
off with an odd-looking function: __init__(). This function is required for classes, and it's used to
initialize the objects it creates. __init__() always takes at least one argument, self, that refers 
to the object being created. You can think of __init__() as the function that "boots up" each object
 the class creates.

Instructions
Remove the pass statement in your class definition, then go ahead and define an __init__() function
 for your Animal class. Pass it the argument self for now; we'll explain how this works in greater 
 detail in the next section. Finally, put the pass into the body of the __init__() definition, since
  it will expect an indented block.
"""

		"""
		class Animal(object):

		    """Constructor"""   #Must type two underscore characters for the name _ + _ + init()
		    def __init__(self): #'self' == 'this', boots up each new object
		        pass #Doesn't do anything but serves as placeholder"
		"""


"""
Let's Not Get Too Selfish
Excellent! Let's make one more tweak to our class definition, then go ahead and instantiate (create) 
our first object.

So far, __init__() only takes one parameter: self. This is a Python convention; there's nothing magic
 about the word self. However, it's overwhelmingly common to use self as the first parameter in
  __init__(), so you should do this so that other people will understand your code.

The part that is magic is the fact that self is the first parameter passed to __init__(). Python will
 use the first parameter that __init__() receives to refer to the object being created; this is why
  it's often called self, since this parameter gives the object being created its identity.

Instructions
Let's do two things in the editor:

Pass __init__() a second parameter, name.
In the body of __init__(), let the function know that name refers to the created object's name by 
typing self.name = name. (This will become crystal clear in the next section.)
"""

		"""
		class Animal(object):

		    """Constructor"""   #Must type two underscore characters for the name _ + _ + init()
		    def __init__(self, name): #'self' == 'this', boots up each new object
		        self.name = name      
		"""


"""
Instantiating Your First Object
Perfect! Now we're ready to start creating objects.

We can access attributes of our objects using dot notation Here's how it works:

class Square(object):
  def __init__(self):
    self.sides = 4

my_shape = Square()
print my_shape.sides

First we create a class named Square with an attribute sides.
Outside the class definition, we create a new instance of Square named my_shape and access that attribute using my_shape.sides.
Instructions
Outside the Animal class definition, create a variable named zebra and set it equal to Animal("Jeffrey").
Then print out zebra's name.
Click "Stuck? Get a hint!" for an example.
"""		
			"""
			class Animal(object):

			    """Constructor"""   #Must type two underscore characters for the name _ + _ + init()
			    def __init__(self, name): #'self' == 'this', boots up each new object
			        self.name = name

			zebra = Animal("Jeffrey")
			print zebra.name	        
			"""


"""
More on __init__() and self
Now that you're starting to understand how classes and objects work, it's worth delving a bit more 
into __init__() and self. They can be confusing!

As mentioned, you can think of __init__() as the method that "boots up" a class' instance object: the
 init bit is short for "initialize."

The first argument __init__() gets is used to refer to the instance object, and by convention, that
 argument is called self. If you add additional arguments—for instance, a name and age for your 
 animal—setting each of those equal to self.name and self.age in the body of __init__() will make it
  so that when you create an instance object of your Animal class, you need to give each instance a
   name and an age, and those will be associated with the particular instance you create.

Instructions
Check out the examples in the editor. See how __init__() "boots up" each object to expect a name and
 an age, then uses self.name and self.age to assign those names and ages to each object? Add a third
 attribute, is_hungry to __init__(), and click Save & Submit Code to see the results.
"""

				"""
				# Class definition
				class Animal(object):
				    """Makes cute animals."""
				    # For initializing our instance objects
				    def __init__(self, name, age, is_hungry):
				        self.name = name
				        self.age = age
				        self.is_hungry = is_hungry

				# Note that self is only used in the __init__()
				# function definition; we don't need to pass it
				# to our instance objects.

				zebra = Animal("Jeffrey", 2, True)
				giraffe = Animal("Bruce", 1, False)
				panda = Animal("Chad", 7, True)

				print zebra.name, zebra.age, zebra.is_hungry
				print giraffe.name, giraffe.age, giraffe.is_hungry
				print panda.name, panda.age, panda.is_hungry
				"""

"""
Class Scope
Another important aspect of Python classes is scope. The scope of a variable is the context in which
 it's visible to the program.

It may surprise you to learn that not all variables are accessible to all parts of a Python program
 at all times. When dealing with classes, you can have variables that are available everywhere 
 (global variables), variables that are only available to members of a certain class (member 
 	variables), and variables that are only available to particular instances of a class (instance 
 	variables).

The same goes for functions: some are available everywhere, some are only available to members of a
 certain class, and still others are only available to particular instance objects.

Instructions
Check out the code in the editor. Note that each individual animal gets its own name and age 
(since they're all initialized individually), but they all have access to the member variable 
is_alive, since they're all members of the Animal class. Click Save & Submit Code to see the output!
"""

		"""
			class Animal(object):
			    """Makes cute animals."""
			    is_alive = True
			    def __init__(self, name, age):
			        self.name = name
			        self.age = age

			zebra = Animal("Jeffrey", 2)
			giraffe = Animal("Bruce", 1)
			panda = Animal("Chad", 7)

			print zebra.name, zebra.age, zebra.is_alive
			print giraffe.name, giraffe.age, giraffe.is_alive
			print panda.name, panda.age, panda.is_alive
		"""

"""
A Methodical Approach
When a class has its own functions, those functions are called methods. You've already seen one such
 method: __init__(). But you can also define your own methods!

Instructions
Add a method, description, to your Animal class. Using two separate print statements, it should print
out the name and age of the animal it's called on. Then, create an instance of Animal, hippo (with 
	whatever name and age you like), and call its description method.

Hint
Remember to pass self as an argument to description. Otherwise, printing self.name and self.age
 won't work, since Python won't know which self (that is, which object) you're talking about!

Your method should look something like this:

def description(self):
    print self.name
    print self.age
After that, all you need to do is create a hippo and call its description method with hippo.description()!
"""			"""
			class Animal(object):
			    """Makes cute animals."""
			    is_alive = True
			    def __init__(self, name, age):
			        self.name = name
			        self.age = age
			        
			    # Add your method here!
			    def description(self):
			        print self.name
			        print self.age
			        
			# Animal hippo = __init__(self, "hippy", 5)  <== Wrong Java-style syntax
			hippo = Animal("hippy", 5)
			hippo.description()
			"""

"""
They're Multiplying!
A class can have any number of member variables. These are variables that are available to all members of a class.

hippo = Animal("Jake", 12)
cat = Animal("Boots", 3)
print hippo.is_alive
hippo.is_alive = False
print hippo.is_alive
print cat.is_alive
In the example above, we create two instances of an Animal.
Then we print out True, the default value stored in hippo's is_alive member variable.
Next, we set that to False and print it out to make sure.
Finally, we print out True, the value stored in cat's is_alive member variable. We only changed the variable in hippo, not in cat.
Let's add another member variable to Animal.

Instructions
After line 3, add a second member variable called health that contains the string "good".
Then, create two new Animals: sloth and ocelot. (Give them whatever names and ages you like.)
Finally, on three separate lines, print out the health of your hippo, sloth, and ocelot.
"""			
			"""
			class Animal(object):
			    """Makes cute animals."""
			    is_alive = True
			    health = "good"
			    def __init__(self, name, age):
			        self.name = name
			        self.age = age
			        
			    # Add your method here!
			    def description(self):
			        print self.name
			        print self.age

			hippo = Animal("hippy", 5)
			hippo.description()
			sloth = Animal("lazy", 1)
			ocelot = Animal("speedy", 1)

			print hippo.health
			print sloth.health
			print ocelot.health
			"""

"""
It's Not All Animals and Fruits
Classes like Animal and Fruit make it easy to understand the concepts of classes and instances, but 
you probably won't see many zebras or lemons in real-world programs.

However, classes and objects are often used to model real-world objects. The code in the editor is a
more realistic demonstration of the kind of classes and objects you might find in commercial software.
 Here we have a basic ShoppingCart class for creating shopping cart objects for website customers;
  though basic, it's similar to what you'd see in a real program.

Instructions
Create an instance of ShoppingCart called my_cart. Initialize it with any values you like, then use
 the add_item method to add an item to your cart.
"""			
class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."

my_cart = ShoppingCart("Jose Luis Castillo")
my_cart.add_item("Bread", 1.3)
my_cart.add_item("Milk", 3.45)
my_cart.add_item("eggs", 1.5)

print my_cart.items_in_cart

"""
Warning: Here Be Dragons
Inheritance is a tricky concept, so let's go through it step by step.

Inheritance is the process by which one class takes on the attributes and methods of another, and 
it's used to express an is-a relationship. For example, a Panda is a bear, so a Panda class could 
inherit from a Bear class. However, a Toyota is not a Tractor, so it shouldn't inherit from the 
Tractor class (even if they have a lot of attributes and methods in common). Instead, both Toyota 
and Tractor could ultimately inherit from the same Vehicle class.

Instructions
Check out the code in the editor. We've defined a class, Customer, as well as a ReturningCustomer 
class that inherits from Customer. Note that we don't define the display_cart method in the body of 
ReturningCustomer, but it will still have access to that method via inheritance. Click Save & Submit
Code to see for yourself!
"""

class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()


"""
Inheritance Syntax
In Python, inheritance works like this:

class DerivedClass(BaseClass):
    # code goes here
where DerivedClass is the new class you're making and BaseClass is the class from which that new
 class inherits.

Instructions
On lines 1-4, we've created a class named Shape.

Create your own class, Triangle, that inherits from Shape, like this:

class Triangle(Shape):
    # code goes here
Inside the Triangle class, write an __init__() function that takes four arguments: self, side1, 
side2, and side3.

Inside the __init__() function, set self.side1 = side1, self.side2 = side2, and self.side3 = side3.

Click "Stuck? Get a hint!" for an example.
"""

class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

"""
Override!
Sometimes you'll want one class that inherits from another to not only take on the methods and 
attributes of its parent, but to override one or more of them.

				class Employee(object):
				    def __init__(self, name):
				        self.name = name
				    def greet(self, other):
				        print "Hello, %s" % other.name

				class CEO(Employee):
				    def greet(self, other):
				        print "Get back to work, %s!" % other.name

				ceo = CEO("Emily")
				emp = Employee("Steve")
				emp.greet(ceo)
				# Hello, Emily
				ceo.greet(emp)
				# Get back to work, Steve!

Rather than have a separate greet_underling method for our CEO, we override (or re-create) the greet
 method on top of the base Employee.greet method. This way, we don't need to know what type of
  Employee we have before we greet another Employee.

Instructions
Create a new class, PartTimeEmployee, that inherits from Employee.

Give your derived class a calculate_wage method that overrides Employee's. It should take self and
 hours as arguments.

Because PartTimeEmployee.calculate_wage overrides Employee.calculate_wage, it still needs to set 
self.hours = hours.

It should return the part-time employee's number of hours worked multiplied by 12.00 (that is, they
 get $12.00 per hour instead of $20.00).
?

"""
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

"""
This Looks Like a Job For...
On the flip side, sometimes you'll be working with a derived class (or subclass) and realize that 
you've overwritten a method or attribute defined in that class' base class (also called a parent or
 superclass) that you actually need. Have no fear! You can directly access the attributes or methods
of a superclass with Python's built-in super call.

The syntax looks like this:

class Derived(Base):
   def m(self):
       return super(Derived, self).m()
Where m() is a method from the base class.

Instructions
------------- 
First, inside your PartTimeEmployee class:

Add a new method called full_time_wage with the arguments self and hours.

That method should return the result of a super call to the calculate_wage method of 
PartTimeEmployee's parent class. Use the example above for help.

Then, after your class:

Create an instance of the PartTimeEmployee class called milton. Don't forget to give it a name.
Finally, print out the result of calling his full_time_wage method. You should see his wage printed 
out at $20.00 per hour! (That is, for 10 hours, the result should be 200.00.)
"""        
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
        
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)
        
milton = PartTimeEmployee("Frank")

print milton.full_time_wage(10)


"""
Class Basics
First things first: let's create a class to work with.

Instructions
Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as 
arguments. Make sure to set these appropriately in the body of the __init__() method (see the Hint
 for more).
"""
class Triangle(object):
    
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3


"""
Class It Up
Great! Now let's add a member variable and a method to our class.

Instructions
Inside the Triangle class:

Create a variable named number_of_sides and set it equal to 3.
Create a method named check_angles. The sum of a triangle's three angles should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.
?
""" 
class Triangle(object):
    
    number_of_sides = 3
    
    def check_angles(self):
        if(self.angle1 + self.angle2 + self.angle3 == 180):
            return True
        else:
            return False
            
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

"""
Instantiate an Object

Let's go ahead and create an instance of our Triangle class.

Instructions
-------------
Create a variable named my_triangle and set it equal to a new instance of your Triangle class. Pass 
it three angles that sum to 180 (e.g. 90, 30, 60).

Print out my_triangle.number_of_sides
Print out my_triangle.check_angles()

"""               
class Triangle(object):
    
    number_of_sides = 3
    
    def check_angles(self):
        if(self.angle1 + self.angle2 + self.angle3 == 180):
            return True
        else:
            return False
            
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        
my_triangle = Triangle(90, 30, 60)
print my_triangle.number_of_sides
print my_triangle.check_angles()

"""
Inheritance

Finally, let's create an Equilateral class that inherits from our Triangle class. (An equilateral 
	triangle is a triangle whose angles are all 60˚, which also means that its three sides are equal
	in length.)

Instructions
------------

Create a class named Equilateral that inherits from Triangle.

Inside Equilateral, create a member variable named angle and set it equal to 60.

Create an __init__() function with only the parameter self, and set self.angle1, self.angle2, and 
self.angle3 equal to self.angle (since an equilateral triangle's angles will always be 60˚).

"""
class Triangle(object):
    
    number_of_sides = 3
    
    def check_angles(self):
        if(self.angle1 + self.angle2 + self.angle3 == 180):
            return True
        else:
            return False
            
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        
my_triangle = Triangle(90, 30, 60)
print my_triangle.number_of_sides
print my_triangle.check_angles()

class Equilateral(Triangle):
    
    angle = 60
    
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle

"""
Class basics
Classes can be very useful for storing complicated objects with their own methods and variables. 
Defining a class is much like defining a function, but we use the class keyword instead. We also use
the word object in parentheses because we want our classes to inherit the object class. This means 
that our class has all the properties of an object, which is the simplest, most basic class. Later 
we'll see that classes can inherit other, more complicated classes. An empty class would look like 
this:

			class ClassName(object):
			    # class statements go here

Instructions
------------
Define a new class named "Car". For now, since we have to put something inside the class, use the 
pass keyword
"""
class Car(object):
    pass


"""
Create an instance of a class
We can use classes to create new objects, which we say are instances of those classes.

Creating a new instance of a class is as easy as saying:

newObject = ClassName()
Instructions
Below your Car class, create a new object named my_car that is an instance of Car.
""" 
class Car(object):
    pass

my_car = Car()

"""
Class member variables
Classes can have member variables that store information about each class object. We call them member variables since they
 are information that belongs to the class object.

Creating member variables and assigning them initial values is as easy as creating any other variable:

class ClassName(object):
    memberVariable = "initialValue"

Instructions
------------
Inside your Car class, replace the pass statement with a new member variable named condition and give it an initial value
 of the string "new".
"""
class Car(object):
    condition = "new"

my_car = Car()


"""
Calling class member variables
Each class object we create has its own set of member variables. Since we've created an object my_car that is an instance
 of the Car class, my_car should already have a member variable named condition. This attribute gets assigned a value as
  soon as my_car is created.

Instructions
-------------
At the end of your code, use a print statement to display the condition of my_car.
"""

print my_car.condition


""""
Initializing a class
There is a special function named __init__() that gets called whenever we create a new instance of a class. It exists by 
default, even though we don't see it. However, we can define our own __init__() function inside the class, overwriting the
 default version. We might want to do this in order to provide more input variables, just like we would with any other 
 function.


The first argument passed to __init__() must always be the keyword self - this is how the object keeps track of itself 
internally - but we can pass additional variables after that.

In order to assign a variable to the class (creating a member variable), we use dot notation. For instance, if we passed 
newVariable into our class, inside the __init__() function we would say:

self.new_variable = new_variable
Instructions
Define the __init__() function of the Car class to take four inputs: self, model, color, and mpg. Assign the last three 
inputs to member variables of the same name by using the self keyword.

Then, modify the object my_car to provide the following inputs at initialization:

model = "DeLorean"
color = "silver"
mpg = 88
You don't need to include the self keyword when you create an instance of a class, because self gets added to the beginning 
of your list of inputs automatically by the class definition.

?
Hint
Creating an instance of a class with many initialization variables looks the same as calling a function with many inputs; 
put all the values in parentheses, separated by commas.

In the body of __init__(), you'd set the model like this:

def __init__(self, model, color, mpg):
    self.model = model
"""

class Car(object):
    condition = "new"
    model = "DeLorean"
    color = "silver"
    mpg = 88
    
    def ___init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg


my_car = Car(self, model, color, mpg)
#my_car = Car("DeLorean", "silver", 88)
#print my_car.condition
#print my_car.model
#print my_car.color
#print my_car.mpg

"""
Referring to member variables
Calling class member variables works the same whether those values are created within the class (like our car's condition)
 or values are passed into the new object at initialization. We use dot notation to access the member variables of classes
  since those variables belong to the object.

For instance, if we had created a member variable named new_variable, a new instance of the class named new_object could
 access this variable by saying:

			new_object.new_variable

Instructions
------------
Now that you've created my_car print its member variables:

First print the model of my_car. Click "Stuck? Get a hint!" for an example.
Then print out the color of my_car.model
Then print out the mpg of my_car.mpg
"""
