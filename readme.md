 # General Commands

 ctrl + l : clear python shell
 exi() : exit python shell

# Types

#### Integers are for representing whole numbers:

```python
rank = 10
eggs = 12
people = 3
```
#### Floats represent continuous values:

```python
temperature = 10.2
rainfall = 5.98
elevation = 1031.88
```

#### Strings represent any text:

```python
message = "Welcome to our online shop!"
name = "John"
serial = "R001991981SW"
```

#### Lists represent arrays of values that may change during the course of the program

```python
members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]
```

#### Dictionaries represent pairs of keys and values

```python
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}
```

#### Keys of a dictionary can be extracted with

```python
phone_numbers.keys()
```

#### Values of a dictionary can be extracted with

```python
phone_numbers.values()
```

#### Tuples represent arrays of values that are not to be changed during the course of the program

```python
vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```
#### To find out what attributes a type has

```python
dir(str)
dir(list)
dir(dict)
```

#### Find out what Python builtin functions there are

```python
dir(__builtins__)
```

#### Documentation for a Python command can be found with

```python
help(str)
help(str.replace)
help(dict.values)
```

# Positive/Negative Indexes, Slicing

#### Lists, strings, and tuples have a positive index system:

```python
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   0      1      2      3      4      5      6
```

#### And a negative index system:

```python
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  -7     -6     -5     -4     -3     -2     -1
```

#### In a list, the 2nd, 3rd, and 4th items can be accessed with

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
```
Output: ['Tue', 'Wed', 'Thu']

#### First three items of a list

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
```
Output:['Mon', 'Tue', 'Wed'] 

#### Last three items of a list

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
```
Output: ['Fri', 'Sat', 'Sun']

#### Everything but the last

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1] 
```
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 

#### Everything but the last two

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2]
```
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 

#### A single in a dictionary can be accessed using its key

```python
phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
phone_numbers["Marry Simpsons"]
```
Output: '+423998200919'


# Conditionals

Using "and" and "or" in a Conditional

#### Check for one single condition

```python
x = 1
 
if x == 1:
    print("Yes")
else:
    print("No")
```
#### Check if two conditions are met at the same time using an and operator

```python
x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")
```
That will return Yes since x == 1 and y ==1 are both True.

#### You can also check if one of two conditions are met using an or operator

```python
x = 1
y = 1
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")
```
That will return Yes since at least one of the conditions is True. In this case x == 1 is True.

# Functions and Conditionals

#### Define a function

```python
def cube_volume(a):
    return a * a * a
```

#### Write a conditional block

```python
message = "hello there"
 
if "hello" in message:
    print("hi")
else:
    print("I don't understand")
```

#### Write a conditional block of multiple conditions:

```python
message = "hello there"
 
if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")
```

#### Use the and operator to check if both conditions are True at the same time:

```python
x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")
```
Output is Yes since both x and y are 1.

#### Use the or operator to check if at least one condition is True:

```python
x = 1
y = 2
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")
```
Output is Yes since x is 1.

#### Check if a value is of a certain type with:

```python
isinstance("abc", str)
isinstance([1, 2, 3], list)
```
or
```python
type("abc") == str
type([1, 2, 3]) == lst
```

# Processing User Input

#### A Python program can get user input via the input function

The input function halts the execution of the program and gets text input from the user

```python
name = input("Enter your name: ")
```

#### The input function converts any input to a string, but you can convert it back to int or float

```python
experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12
```

#### You can format strings with (works both on Python 2 and 3)
```python
name = "Sim"
experience_years = 1.5
print("Hi %s, you have %s years of experience." % (name, experience_years))
```
Output: Hi Sim, you have 1.5 years of experience.

#### You can also format strings with (Python 3 only)

```python
name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
```
Output: Hi Sim, you have 1.5 years of experience.

# For Loop Over a Function

#### Call any function multiple times, even your own functions.

Let's suppose we defined this function:

```python
def celsius_to_kelvin(cels):
    return cels + 273.15
```

That is a function that gets a number as input, adds 273.15 to it and returns the result.

#### A for loop allows us to execute that function over a list of numbers

```python
monday_temperatures = [9.1, 8.8, -270.15]
 
for temperature in monday_temperatures:
    print(celsius_to_kelvin(temperature))
```
The output of that would be:

- 282.25
- 281.95
- 3.0

So, in the first iteration celsius_to_kelvin(9.1) was executed, in the second celsius_to_kelvin(8.8) and in the third celsius_to_kelvin(-270.15).

# Dictionary Loop and String Formatting

#### Combine a dictionary for loop with string formatting to create text containing information from the dictionary:

```python
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))
```

Another (better) way to do it::

```python
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))
```
In both cases the output is:
- John Smith has as phone number +37682929928
- Marry Simpons has as phone number +423998200919

# Loops

#### Loops are useful for executing a command over a large number of items.


```python
for letter in 'abc':
    print(letter.upper())
```
Output:
- A
- B
- C

The name after for (e.g. letter) is just a variable name

#### Loop over dictionary keys

```python
phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.keys():
    print(value)
```
Output:
- John Smith
- Marry Simpsons

#### Loop over dictionary values

```python
phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.values():
    print(value)
```
Output:
- +37682929928
- +423998200919

#### Loop over dictionary items

```python
phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for key, value in phone_numbers.items():
    print(key, value)
```
Output: 
- ('John Smith', '+37682929928')
- ('Marry Simpons', '+423998200919')

#### While loops will run as long as a condition is true:

```python
while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    print("It's not yet 19:30:20 of 2090.8.20")
```
The loop above will print out the string inside print() over and over again until the 20th of August, 2090.

# List Comprehensions

A list comprehension is an expression that creates a list by iterating over another container.

#### A basic list comprehension

```python
[i*2 for i in [1, 5, 10]]
```
Output: [2, 10, 20]

#### List comprehension with if condition

```python
[i*2 for i in [1, -2, 10] if i>0]
```
Output: [2, 20]

#### List comprehension with an if and else condition

```python
[i*2 if i>0 else 0 for i in [1, -2, 10]]
```
Output: [2, 0, 20]

# More on Functions

#### Functions can have more than one parameter

```python
def volume(a, b, c):
    return a * b * c
```

#### Functions can have default parameters (e.g. coefficient)

```python
def converter(feet, coefficient = 3.2808):
    meters = feet / coefficient
    return meters
 
print(converter(10))
```
Output: 3.0480370641306997

### Arguments can be passed as non-keyword (positional) arguments (e.g. a) or keyword arguments (e.g. b=2 and c=10)

```python
def volume(a, b, c):
    return a * b * c 
print(volume(1, b=2, c=10))
```

### An *args parameter allows the  function to be called with an arbitrary number of non-keyword arguments

```python
def find_max(*args):
    return max(args)
print(find_max(3, 99, 1001, 2, 8))
```
Output: 1001

#### An **kwargs parameter allows the function to be called with an arbitrary number of keyword arguments

```python
def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
```
Output: Sim

#### Summary of function elements:

![](/assets/img/functionsPython.png)

# File Processing

#### Read an existing file with Python

```python
with open("file.txt") as file:
    content = file.read()
```
#### Create a new file with Python and write some text on it

```python
with open("file.txt", "w") as file:
    content = file.write("Sample text")
```

#### Append text to an existing file without overwriting it

```python
with open("file.txt", "a") as file:
    content = file.write("More sample text")
```

#### Both append and read a file with

```python
with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()
```

# Imported Modules

Builtin objects are all objects that are written inside the Python interpreter in C language.

Builtin modules contain builtins objects.

Some builtin objects are not immediately available in the global namespace. They are parts of a builtin module. To use those objects the module needs to be imported first. E.g.:

```python
import time
time.sleep(5)
```

A list of all builtin modules can be printed out with:

```python
import sys
sys.builtin_module_names
```
Standard libraries is a jargon that includes both builtin modules written in C and also modules written in Python.

Standard libraries written in Python reside in the Python installation directory as .py files. You can find their directory path with sys.prefix.

Packages are a collection of .py modules.

Third-party libraries are packages or modules written by third-party persons (not the Python core development team).

Third-party libraries can be installed from the terminal/command line:

Windows:

```python
pip install pandas
```

Mac and Linux:

```python
pip3 install pandas
```


# The any() function

if not any(website in line for website in website_list) part in the previous video, here is another example:

```python
>>> lines  = ["trees are good", "pool is fresh", "face is round"]
>>> website_list = ["face", "clock", "trend"]
>>> for line in lines:
...     any(website in line for website in website_list)
... 
False
False
True
```

We start iterating over the items of website_list using a for loop. In the first iteration we would have:

```python
any(website in "trees are good" for website in website_list)
```
Inside the parenthesis of any() there's another loop that iterates over website_list:

```python
("face" in "trees are good")
("clock" in "trees are good")
("trend" in "trees are good")
```

If any of the above is True you get the expression evaluated to True. In this case none of them is True, so you get False.

If you want to return True (if all of them are True), use all() instead of any().

So, the part any(website in line for website in website_list) will either be equal to True or False.



# Useful commands

#### Check wich modules are installed
```python
pip3 freeze
```

#### Check python version of the terminal you're using

For some reasons, an imported module in your favorite terminal may be not found in the terminal of your favorite IDE. It's then interested to check the python version of IDE's terminal.

```pyhton
Francois at Mycomputer in ~/WorkspacePython/app4/webapp (master●●)
$ python3
Python 3.7.6 (default, Dec 30 2019, 19:38:26) 
[Clang 11.0.0 (clang-1100.0.33.16)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.version
'3.7.6 (default, Dec 30 2019, 19:38:26) \n[Clang 11.0.0 (clang-1100.0.33.16)]'
>>> sys.executable
'/usr/local/opt/python/bin/python3.7'
>>> 
```

Both python version should be the same (3.7 in this specific case)