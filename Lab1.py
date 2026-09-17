# Lab 1 of AI
# Introduction to AI and Its Application Using Python

# Task 1: Execute a simple Python syntax example.
print("Hello, World!")


# Task 2: Comments in Python.
x = 1  # This is an inline comment.
print("These are two comments")  # Print a string.


# Task 3: Input and output.
txt = input("Type something to test this out: ")  # Take input from the user.
print(txt)  # Display the entered text.


# Task 4: Multiple statements on a single line.
print("Statement1"); print("Statement2")  # Two statements use a semicolon.


# Task 5: Indentation using one space.
x = 1
if x > 0:
    print("This statement has a single space indentation.")
    print("This statement has a single space indentation.")


# Task 6: Indentation using a tab.
x = 1
if x > 0:
    print("This statement has a single tab indentation.")
    print("This statement has a single tab indentation.")


# Task 7: Indentation using four spaces according to Python coding style.
x = 1
if x > 0:
    print("This statement has four spaces indentation.")
    print("This statement has four spaces indentation.")


# Task 8: Integer data type.
a = 1452  # Store an integer value.
print(type(a))

b = -4587  # Store a negative integer.
print(type(b))

c = 0  # Store zero as an integer.
print(type(c))


# Task 9: Floating-point data type.
g = 1.03  # Store a positive floating-point value.
print(type(g))

h = -11.23  # Store a negative floating-point value.
print(type(h))

i = .34  # Store a floating-point value without a leading zero.
print(type(i))

j = 2.127e-10  # Store a floating-point value in scientific notation.
print(type(j))

k = 5E220  # Store a large floating-point value.
print(type(k))


# Task 10: Complex data type.
x = complex(1, 2)  # Create a complex number using complex().
print(type(x))
print(x)

z = 14 + 24j  # Create a complex number using real and imaginary parts.
print(type(z))

z = 14 + 27j  # Assign another complex number.
print(type(z))


# Task 11: Boolean data type.
x = True  # Store the Boolean value True.
print(type(x))

y = False  # Store the Boolean value False.
print(type(y))


# Task 12: Creating strings.
str1 = "String"  # Strings can start and end with double quotes.
print(str1)

str2 = 'String'  # Strings can also start and end with single quotes.
print(str2)

str2 = "Day's"  # A single quote can be used inside double quotes.
print(str2)

str2 = '"Day"s'  # Double quotes can be used inside a single-quoted string.
print(str2)


# Task 13: Special characters in strings.
print("The is a backslash (\\) mark.")  # Display a backslash.
print("This is tab \t key")  # Use \t to insert a horizontal tab.
print("These are \'single quotes\'")  # Use escaped single quotes.
print("These are \"double quotes\"")  # Use escaped double quotes.
print("This is a new line\nNew line")  # Use \n to create a new line.


# Task 14: String indices and accessing string elements.
string1 = "PYTHON TUTORIAL"  # Create the string used for indexing.

print(string1[0])  # Print the first character.
print(string1[-15])  # Print the first character using a negative index.
print(string1[14])  # Print the last character.
print(string1[-1])  # Print the last character using a negative index.
print(string1[4])  # Print the fifth character at index 4.
print(string1[-11])  # Access the same character using a negative index.


# Task 15: String slicing.
print(string1[3:7])  # Slice characters from index 3 up to, but not including, 7.
print(string1[1:5])  # Slice a substring using two indices.
print(string1[:6])  # Slice from the beginning to index 5.
print(string1[6:])  # Slice from index 6 to the end.


# Task 16: Creating lists.
my_list1 = [5, 12, 13, 14]  # Create a list containing integer values.
print(my_list1)

my_list2 = ["red", "blue", "black", "white"]  # Create a list of strings.
print(my_list2)

my_list3 = ["red", 12, 112.12]  # Create a list with mixed data types.
print(my_list3)

my_list = []  # Create an empty list.
print(my_list)


# Task 17: List indices.
color_list = ["RED", "Blue", "Green", "Black"]  # Create a list with four elements.

print(color_list[0])  # Return the first element.
print(color_list[0], color_list[3])  # Print the first and last elements.
print(color_list[-1])  # Return the last element.


# Task 18: List slicing.
print(color_list[0:2])  # Cut the first two items.
print(color_list[1:2])  # Cut the second item.
print(color_list[1:-2])  # Slice using a negative end index.
print(color_list[:3])  # Cut the first three items.
print(color_list[:])  # Create a copy of the original list.


# Task 19: Conditional statements.
a = 10  # Store the first value.
b = 20  # Store the second value.

if b > a:  # Check whether b is greater than a.
    print("b is greater than a")
