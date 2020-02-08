# Comments

Used to explain code, make the code more readable and prevent execution when testing code

Single line comments (hash symbol)

Multi line comments (Triple quotes)

Best practices (keep it short, straight to the point, and informative, D.R.Y)

Docstrings

```python
#This is a comment
print("Hello, World!")

print("Hello, World!") #This is a comment

#print("Hello, World!")
print("Cheers, Mate!")

#This is a comment
#on more than
#just one line
print("Hello, World!")

#This is a comment
#on more than
#just one line
print("Hello, World!")

"""
This is a comment
on more than
just one line
"""
print("Hello, World!")

# Storing the number 5 in the variable x (bad comment)
x = 5
```

Exercises:

Write a single line comment and a multi line comment

Print out “Hello World”, comment it out and run it again 

# Data Types

Booleans

Integers

Floating point numbers

Strings

Note: There is a 5th data type: complex numbers

# Boolean Data Type

In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

True and False are built-in keywords

True is represented by 1

False is represented by 0

Bool()

# Numeric Data Types

Integers: is a whole number, positive or negative, without decimals

Floating point numbers: is a number, positive or negative, containing one or more decimals

type()

Type conversion (int(), float())

```python
type(5)
type(4.5)
print(float(10))
print(int(3.1434))
print(float(-4.22))
print(int(-3))
```


Exercises:

Convert 5 into a float and convert 5.2 into an int

What is the value of max(5,3)? Hint: look up built-in functions in python

# Strings

Defining a string: str() or Single or double quotations

Multi line strings

Type conversion (int to strings, strings to ints only if you know it’s an int, otherwise it will be an error)

Accessing elements using index from the front and the back

Slicing range (important): String_object[start_pos : end_pos : step]

Len()

Format()

```python
print(‘hello’)
print(“hello”)
print(“””
this is a long string
on multiple lines
“””)
print(str(5))
print(int(“30”))
print(int(“hello”))
print(“hello”[0])
print(“hello”[-1])
print(“hello”[2:3])
print(“hello”[2:5:2])
print(“hello”[-4:-2])
print(len(“bootcamp”))
print(“My fav int is {}”.format(24))
print(“I want to buy {0} for {1} dollars”.format(“fruits”, “5”))
```

Exercises:

Print the 6th character of the following string: “python is powerful”

Print the second last digit of the following int: 123456

Print the following string in reverse: “hello”. Hint: use [start:stop:step]

Print the following string in lowercase: “HELLO”. Hint: Look up string methods in python

# Operators

Arithmetic Operators

(+, -, *, /, //, **, %)

Addition

Subtraction

Multiplication

Division (always returns float)

Floor Division (rounds down)

Exponents

Modulus

```python
print(5+5)
print(“hello” + “world”)
print(1-8)
print(2*2)
print(“woo”*3)
print(10/4)
print(10//4)
print(-10/4)
print(3**3)
print(20%9)
print(1 + 2/5 * 4 – (2**2))
```
Written using regular mathematical notation

If combining two Int values, the result is an Int

If combining two Float values, or a Float and an Int, the result is a Float

Assignment Operators

(+=, -=, *=, /=, //=, **=)


Comparison Operators

(==, !=, >, <, >=, <=)

Equal

Not Equal

Greater Than

Less than

Greater than or equal to

Less than or equal to

```python
print(5==5)
print(1!=2)
print(6>7)
print(3<9)
print(7 >= -2)
print(120 <= 250)
```

Logical Operators

And

Or

Not

```python
print(5==5 and 6 > 4)
print(1 < 2 and 5 >= 3)
print(5==5 or 6 < 4)
print(1 < 2 or 5 <= 3)
print(not(1 != 1))
```

Membership Operators

In

Not in

```python
print(“s” in “soup”)
print(“ts” in “times”)
print(“w” not in “something”)
print(“r” not in “rhyme”)
```

Notes: There are two more types of operators: Bitwise and Identity

Exercises:

What is the value of: not(“a” not in “a” and -5//4 == 0 or 2==2) and False?

# Variables

Variables are containers for storing data values

Assignment statements (v = expr)

Can change after assignment: not just the current value but the data type as well

Assignment operator (+=, -=, *=, /=, //=, **=)

Assign multiple values to multiple variables in one line

Assign the same value to multiple variables in one line

Short names or a more descriptive name

A variable name must start with a letter or the underscore character

- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- Best practices (PEP8)

```python
x = 5
print(x)
x = “python is the best”
print(x)
x,y,z = 1,2,3
print(x, y, z)
x = y = z = 1
print(x, y, z)
age = 20
Age = 21
AGE = 22
print(age)
x = 25
x += 5
print(x)
```

Exercises:
	
Use as few lines as possible
	
1. Compute your age using your birth year and the current year and store it in a variable
2. Double your age and store it in the same variable
3. Why can’t we write int = 5 and what should we use instead? Hint: Look up trailing underscores in PEP8. 


# Data Structures

List


Tuple

Set

Dict

Data structure is basically an abstract way of organizing data.

There are a few more but we are only going to focus on the most used ones.

# Lists (arrays)

A collection which is ordered and changeable. Allows duplicate members.

Defining a list: list(iterable) or written with square brackets

Accessing elements using index (negative index, slice range)

Updating items

Adding items (insert(), append())

Removing items (del: deletes the value at index, remove(): remove the first matching value, pop(): deletes and return the value at index)

Len()

```python
fruits = ["apple", "banana", "cherry", “apple”]
print(fruits[0])
print(fruits[-1])
print(fruits[6])
fruits[1] = 70.45
print(fruits)
print(fruits[1:3])
print(“banana” in fruits)
fruits.append(“oranges”)
item = fruits.pop()
print(item)
fruits.remove(“apple”)
del fruits[0]
print(len(fruits))
```

Exercises:

Create a list of 4 floating point numbers and 2 strings and 1 boolean 

Add two 2 new elements to the list

Change the first element to 24

Delete all elements that are strings and booleans

Switch the first element in the list with the last element

Sort the list. Hint: Look up list methods in python
	
# Tuples

A collection which is ordered and immutable. Allows duplicate items.

Defining a tuple: tuple(iterable) or written with round brackets

Tuple with one item

Accessing items using index (negative index, slice range)

Updating items (we can’t)

Adding items (we can’t)

Deleting items

Len(), count(), index()

```python
fruits = ("apple", "banana", "cherry", “apple”)
print(fruits[0])
print(fruits[-1])
print(fruits[6])
fruits[1] = “grapes”
print(fruits[1:3])
print(“banana” in fruits)
fruits.pop()
fruits.remove(“apple”)
del fruits[0]
print(len(fruits))
```

Exercises:

Create a tuple and play around with it, try accessing, adding, updating and deleting elements

Given a tuple (1,2,2,3). Find the index of element 2. Hint: look up tuple methods in python.

# Sets

A set is a collection which is unordered and unindexed. No duplicate members.

Defining a set: set(iterable) or written with curly brackets, empty {} is reserved for dictionaries

Accessing items (cannot use an index)

Adding items (add(), update())

Removing items (remove(), what happens if we try removing an item not in the set?, discard())

Len(), union()

```python
fruits = {"apple", "banana", "cherry", “apple”}
print(fruits)
print(fruits[0])
fruits.add(“oranges”)
print(“banana” not in fruits)
fruits.pop()
fruits.remove(“watermelon”)
fruits.discard(“watermelon”
print(len(fruits))
```

Exercises:
Create a set and try accessing the 1st element using the index. What happens?

Given two sets such as {1,2, 3} and {3,4,5}. Find the common elements shared by both sets. Hint: look up sets methods in python.

Store an empty set {} in a variable and print its type. What does it say?


# Dictionaries

A dictionary is a collection which is unordered, changeable and indexed.

Have keys and values

Defining a dict: dict() or written with curly brackets

Accessing items (key name, get())

Updating items

Adding items

Removing items (del, pop())

```python
MLB _team = {
'Colorado': 'Rockies',
'Boston': 'Red Sox',
'Minnesota': 'Twins',
'Milwaukee': 'Brewers',
'Seattle': 'Mariners'
}
MLB _team
MLB _team[‘Minnesota’]
MLB _team[‘Toronto’]
MLB_team.get(“Toronto”)
MLB_team['Kansas City'] = 'Royals'
MLB_team['Seattle'] = 'Seahawks'
del MLB_team['Seattle']
MLB_team.pop(“Boston”)
“Vancover” in MLB_team
```

Exercises:

Create a dict and play around with accessing, updating, adding and removing elements.

Create a dict of length 5, with keys of type int and values of type list.


# Control Flow

There has always been a series of statements faithfully executed by Python in exact top-down order. What if you wanted to change the flow of how it works? For example, you want the program to take some decisions and do different things depending on different situations, such as printing 'Good Morning' or 'Good Evening' depending on the time of the day?

# If…elif…else

```python
If condition:
	Statement1
	…
Elif condition1:
	Statement2
	…
Else:
	Statement3
	…
```

If checks the truth of an expression

Evaluates to a Boolean, True or False

Depending on the Boolean, it will either execute the statements or skip over it

Indentation and whitespace are important

If with elif and else

Nested statements

The program will evaluate the condition, if its true, then it will execute statement1 otherwise it will evaluate condition1, if it’s true, then it will execute statement2 otherwise, it will execute statement3

```python
num = 20
if num > 0:
    if num >= 10:
        print("10")
    else:
	    print("Positive number greater than 10")
elif num == 0:
	print("Zero")	
else:
    print("Negative number")
```

Exercises:

Given a number n. Print “tricky” if it’s a zero, “yes” if its an even number, otherwise, “no”. Hint: to check if a number is even, use the modulo operator.

Given a list of strings x. Print “empty” if the list has no elements, print “found it” if “cheese” is in the list, otherwise, print “did not find it”.


# For Loop

A for loop is used for iterating over a sequence (list, a tuple, a dictionary, a set, or a string)

break: With the break statement we can stop the loop before it has looped through all the items

continue: With the continue statement, we can stop the current iteration of the loop, and continue with the next

range(start, end, step): returns a sequence of numbers from start (included) to end (excluded) incremented by step. Start is 0 by default and step is 1 by default. End always needs to be specified.

enumerate(iterable, start=0): An easy way to keep count of iterations along with the items in iterable

```python
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
for val in numbers:
    sum = sum+val
print("The sum is", sum)

```
Exercises:

Given a dict, store all the keys in a new list and print it at the end.

Print each character in your name along with its index position.

Print all the numbers from 0 to 100, except 25.

Given a list l and a number n. Print all elements in the list up till n, if n is in the list.

# While Loop

With the while loop, we can execute a set of statements as long as a condition is true.

We generally use this loop when we don't know beforehand, the number of times to iterate.

break: With the break statement we can stop the loop before it has looped through all the items

continue: With the continue statement, we can stop the current iteration of the loop, and continue with the next

Infinite Loop: a loop that never ends

```python
i = 0
while i < 10:
    print(i)
    i += 1 
```

Exercises:

Write an infinite loop

Given a list of numbers, separate them into two new lists, first list for odd numbers and the second list for even numbers

Given a number n, calculate its factorial and print it.




# Functions

A function is a group of related code statements that perform a certain task and the function only runs when it is called.

Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable. It also avoids repetition and makes code reusable.

Defining: It is defined using the def keyword followed by the function name and parentheses

Calling: To call a function, use the function name followed by parenthesis

Parameters/Arguments: specified inside the parenthesis. Add as many as you want, separated by commas. It can be of any type.

Default parameter values

Return: to return a value, use the return function. Important: returning is not necessary.

Arbitrary Arguments *args

Keyword Arguments

Arbitrary Keyword Arguments, **kwargs

Scope of variables: Variables that are defined inside a function body have a local scope, and those defined outside have a global scope. This means that local variables can be accessed only inside the function in which they are declared, whereas global variables can be accessed throughout the program body by all functions. 

```python
def fn_name(parameter(s)):
	…
	…
	return
```

Exercises:

Write a function that takes two parameter values of type integer, x and y and returns the smaller number.

Write a function that takes an optional parameter, and prints the parameter if provided, otherwise prints “no” 

Write a Python function that takes a list and returns a new list with unique elements from the first list



# I/O

In the real world, you will most likely be dealing with databases rather than user input or files. 

# stdin & stdout

Up till now, our programs were static. The value of variables were defined or hard coded.

To allow flexibility, we might want to take input from the user.

Reading from stdin: Use input(prompt). Prompt is an optional argument. This pauses the program execution till the user presses the enter key. All characters typed are read and returned as a string.

print(): converts the expressions you pass into a string and writes the result to standard output

Formatting: Use format() to format a string

```python
name = input(“What is your name? “)
```

Exercises:

Write a function that takes input of length and breadth of a rectangle from user and prints the area of it.

Write a function that keeps asking user for a number till nothing is entered. Store the numbers in a list and print it. 

# Files

Open(filename, mode)

Types of mode
- "r" - Read - Default value. Opens a file for reading, error if the file does not exist
- "a" - Append - Opens a file for appending, creates the file if it does not exist
- "w" - Write - Opens a file for writing, creates the file if it does not exist
- "x" - Create - Creates the specified file, returns an error if the file exists
- File objects contain methods that can be used to read information about the file you opened

Reading from a file

Creating or Writing to a file

Closing a file

With statement

```python
with open(“filename”) as file:
	…
	…
```

Exercises:

Create a text file with lyrics from your favorite song and close it

Open your file and append lyrics from your favorite song, close it

Open your file and print each line one by one.

# Exceptions

An exception is a Python object that represents an error. A program will raise an exception when it encounters a situation it cannot deal with.

Handing exceptions:
- The assert statement
- Try/Except/Else
- Try/Finally

Raising an exception

Exercises:

Write a function that takes two parameters, a list l and a number n, and returns the element at the index n in the list.


# Modules

Module: is simply a file consisting of Python code. Generally, its large programs split into different files for easier maintenance, reusability and better performance

Why is it useful: modules and libraries provide extra functionality

Import statement: This allows you to import all functionality from a module. Use the import keyword followed by the module name to make it available in your file.

From import statement: This allows you to import specific functions/variables from a module instead of importing everything. Use the from keyword followed by the module name followed by the import keyword followed by the specific function or variable name you want.

Importing as alternate names using the as keyword

```python
Import module_name as md
```

Exercises:

Write a function that takes two parameters, x and y, and returns a random number between x and y, inclusive. Hint: import the random module

Write a function that prints the current date and time. Hint: use the datetime module


# Data Science Process

Gather

Clean

Explore

Model

Evaluate

# Data Analysis Libraries

Pandas

Numpy

MatplotLib
