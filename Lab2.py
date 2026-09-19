# ==============================================================
#                         ARTIFICIAL INTELLIGENCE
#                              LAB NO. 02
# ==============================================================
# Topic: Iterative Structures in Python
# ==============================================================
# Name: __Shahwaiz ALi____________________________
# Roll No: _____BS_IT_24_M_38______________________
# Section: _________IT_______________
# ==============================================================


# --------------------------------------------------------------
# WHILE LOOP
# --------------------------------------------------------------

# Python program to illustrate
# while loop

count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")


# --------------------------------------------------------------
# SINGLE STATEMENT WHILE BLOCK
# --------------------------------------------------------------

# Python program to illustrate
# Single statement while block

count = 0
while (count == 0):
    print("Hello Geek")
    count = 1


# --------------------------------------------------------------
# FOR IN LOOP - LIST ITERATION
# --------------------------------------------------------------

# Python program to illustrate
# Iterating over a list

print("List Iteration")
l = ["geeks", "for", "geeks"]

for i in l:
    print(i)


# --------------------------------------------------------------
# FOR IN LOOP - TUPLE ITERATION
# --------------------------------------------------------------

# Iterating over a tuple (immutable)

print("\nTuple Iteration")
t = ("geeks", "for", "geeks")

for i in t:
    print(i)


# --------------------------------------------------------------
# FOR IN LOOP - STRING ITERATION
# --------------------------------------------------------------

# Iterating over a String

print("\nString Iteration")
s = "Geeks"

for i in s:
    print(i)


# --------------------------------------------------------------
# ITERATING BY INDEX OF SEQUENCES
# --------------------------------------------------------------

# Python program to illustrate
# Iterating by index

list_data = ["geeks", "for", "geeks"]

for index in range(len(list_data)):
    print(list_data[index])


# --------------------------------------------------------------
# CONTINUE STATEMENT
# --------------------------------------------------------------

# Prints all letters except 'e' and 's'

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue

    print('Current Letter :', letter)


# --------------------------------------------------------------
# BREAK STATEMENT
# --------------------------------------------------------------

for letter in 'geeksforgeeks':
    # break the loop as soon as it sees 'e'
    # or 's'

    if letter == 'e' or letter == 's':
        break

    print('Current Letter :', letter)


# --------------------------------------------------------------
# PYTHON FUNCTIONS
# --------------------------------------------------------------

# Creating a Function

def my_function():
    print("Hello from a function")


# Calling a Function

my_function()


# --------------------------------------------------------------
# PARAMETERS
# --------------------------------------------------------------

# Function with one parameter

def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


# --------------------------------------------------------------
# DEFAULT PARAMETER VALUE
# --------------------------------------------------------------

def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# --------------------------------------------------------------
# PASSING A LIST AS A PARAMETER
# --------------------------------------------------------------

def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)


# --------------------------------------------------------------
# RETURN VALUES
# --------------------------------------------------------------

def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


# --------------------------------------------------------------
# KEYWORD ARGUMENTS
# --------------------------------------------------------------

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# --------------------------------------------------------------
# PYTHON CLASSES / OBJECTS
# --------------------------------------------------------------

# Create a class named MyClass, with a property named x

class MyClass:
    x = 5


# Create an object named p1, and print the value of x

p1 = MyClass()
print(p1.x)


# --------------------------------------------------------------
# THE __INIT__() FUNCTION
# --------------------------------------------------------------

# Create a class named Person, use the __init__() function
# to assign values for name and age

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# --------------------------------------------------------------
# OBJECT METHODS
# --------------------------------------------------------------

# Insert a function that prints a greeting,
# and execute it on the p1 object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()
