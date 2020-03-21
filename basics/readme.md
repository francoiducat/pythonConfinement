 # General Commands

 ctrl + l : clear python shell

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
