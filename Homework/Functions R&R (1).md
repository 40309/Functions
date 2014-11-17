#Reading and Research - Functions

These tasks are designed to introduce you to the programming topic we will be studying in class next lesson. You **must** complete these activities prior to the lesson.

##Functions
A function is a way of segmenting code into manageable pieces, so that it can be used again and again. Creating functions cuts the size of scripts and makes them easier to understand.

You have been using functions since you started learning Python. Two of the most common are `input()` and `print()`.

When a function is used in the main body of your program it is called a function call. You can recognise a function call as it has the following features:

![](https://www.dropbox.com/s/pmd6rfshxe3nelk/function_example.jpg?dl=1)

##Parameters
Most functions work on some data that is provided by the main program. The data is passed from the main program to the function by putting it between the brackets of the function call. Multiple pieces of data are separated with commas. These pieces of data are the **parameters** of the function.

A function can have **zero or more parameters**. If it has zero parameters, the brackets are empty.

##Built-in functions
The Python interpreter has a number of functions and types built into it that are always available. You have already met a number of these.

###Task 1
Use the Python shell to investigate the built-in functions below and complete the table.

|Code|Result|Description of function|
|----|------|-----------------------|
|`round(3.87)`|*4*|*It rounds the number to the nearest integer*|
|`round(3.5)`|*4*|*It rounds the number to the nearest integer*|
|`round(4.5)`|*5*|*It rounds the number to the nearest integer*|
|`round(5.78,1)`|*5.8*|*It rounds the number to the first decimal place*|
|`str(7)`|*7*|*Return a string containing a nicely printable representation of an object*|
|`str(7.65)`|*7.65*|*Return a string containing a nicely printable representation of an object*|
|`len("Computing")`|*9*|*count character length of the string*|
|`type(7)`|*class 'int'*|*Informs what type of data has been entered*|
|`type("7")`|*class 'str'*|*Informs what type of data has been entered*|
|`chr(97)`|*a*|*Return a string of one character whose ASCII code is the integer*|
|`ord("a")`|*97*|*Opposite of **chr*** *Given a string of length one, return an integer representing the Unicode code point |

##String Functions
Python has a number of built-in functions that allow a programmer to manipulate text strings.

###Task 2
Find out what each of the string functions in the table below does to a text string variable with the identifier msg. You will need to assign msg a value that is a string with a mix of upper and lower case letters and multiple words and then explore the effects of each of the functions.

|Function|Effect it has on text string|
|--------|----------------------------|
|`msg.upper()`|*Makes all the letters upper case*|
|`msg.lower()`|*Makes all the letters lower case*|
|`msg.capitalize()`|*Capitalizes all the letters*|
|`msg.title()`| |

###Task 3

1. Write a program that reads in a string and displays the number of characters in the string.
2. Write a program that displays the ASCII code for any given character.
3. Write a program that will display the character for any given ASCII code.

Paste your code and screenshots of running your programs in the space below

```python
#question 1
user_input = input("Please enter your string: ")
length = len(user_input)
print(length)
```

![Running Question 1 program](https://www.dropbox.com/s/tb719a7qsmr094h/code%201.JPG?dl=1)

```python
#question 2
user_input = input("Please enter your value or string of one character: ")
ascii = ord(user_input)
print(ascii)
```

![Running Question 2 program](https://www.dropbox.com/s/3ixdsjyicdsm0b8/Code%202.JPG?dl=1)

```python
#question 3
user_input = int(input("Please enter your ASCII value: "))
ascii = chr(user_input)
print(ascii)
```

![Running Question 3 program](https://www.dropbox.com/s/j9vtkf3rlhl32ek/code%203.JPG?dl=1)

##Importing Modules
A module is a group of functions that programmers have packaged together for people to use. To use a module in your code you must import it into your program.

You do this by adding a line at the top of your program e.g.

`import math`

When calling a function that is part of a module you need to prefix the function name with the module identifier, using dot notation e.g.

`math.trunc(my_float)`

###Task 4

1. Use the [Python Documentation](https://docs.python.org/3/) to find out about the functions in the table below

    |Math Function|Description|
    |-------------|-----------|
    |`math.trunc(3.14159)`| *It just removes the fractional part of the number and leaves the integer*|
    |`math.pi`| *Gives you pi, to precise accuracy*|
    |`round(math.pi, 3)`|*rounds number to 3 decimal places*|

2. Using the Python documentation, identify two other useful functions in the math module, briefly describe what each does and give a brief example of the purpose of a program that might use this function.

    |Math Function|Description|Program that would use it|
    |-------------|-----------|-------------------------|
    |math.cos()|*the trigonometric function that is equal to the ratio of the side adjacent to an acute angle (in a right-angled triangle) to the hypotenuse.*|*working out the angle in a Triangle*|
    |math.log()|*In mathematics, the logarithm of a number is the exponent to which another fixed value, the base, must be raised to produce that number. *|*|

##Using Built-in Functions and Modules
Let's consider some code that uses some of the built-in functions that you have been investigating.

###Task 5
Without entering the code into Python, try to explain what the code below does. You will need to explain each of the different sections of the program by **adding comments** to the program.

```python
import math

number_to_change = float(input("Please enter a number to 3 or more decimal places: "))#get user input, eg 3.14159
number_one = math.trunc(number_to_change)#Gets the integer part of the number, eg 3
number_two = round(number_to_change,2)#rounds the number to 2 decimal places, eg 3.14

print("The integer part of your number is {0}.".format(number_one))#prints number_one, eg "3"
print("The number to two decimal places is {0}.".format(number_two))#prints number_two, eg "3.14"
```

##Structured programming
Read **pages 84 and 85** of AS Computing by Bond and Langfield which describe structure tables and hierarchy charts.

###Task 6
Complete the following statements about structure tables

1. A structure table shows how a problem can be *broken down, to make it easier to solve the problem*
2. The steps involved in solving a problem are written as *modules*.

Consider this problem:

####Roasting Time For Chickens
*A program is needed that works out the cooking time for roasting a chicken. The time required is 30 minutes for every 500g plus 30 minutes. If the chicken is stuffed, it needs an extra 30 minutes. The user enters the weight of the chicken in grams and whether it is stuffed, and the program calculates the approximate time it should be roasted for in hours and minutes.*

The problem above can be divided into simpler sub-problems that make writing the program easier:

- Get weight of chicken from user.
- Get whether chicken is stuffed or not from user.
- Calculate total roasting time.
- Display roasting time.

The third sub-problem, calculating the total roasting time, involves some sub-problems itself:

- Calculate roasting time for weight in minutes.
- Add additional 30 minutes required.
- Add time if chicken is stuffed (further 30 minutes).
- Convert minutes cooking time to hours and minutes.

###Task 7
Produce a structure table for the **Roasting time for chickens** problem.

###Task 8
Draw a hierarchy chart for the 'Roasting time for chickens' problem.

![Hierarchy chart](https://www.dropbox.com/s/wrsqz5j5eiy6oem/Hierarchy%20chart.PNG?dl=1)

##Summary
In this R&R you have investigated built-in functions and importing modules. You have seen the basic structure of a function call and how parameters can be passed to a function. You have also seen how to import modules so that their functions are available in your program. You have investigated functions in the random module and the math module.

You have also explored structure tables and hierarchy charts. These are approaches to program design that help in the breakdown of more complex problems into sub-problems. This makes it easier to develop programs to address more complex problems.

Please make sure you have completed this R&R fully before your next programming lesson as it will form the basis of the initial classroom discussion and starter tasks.


