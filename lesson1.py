
## Learning math operators in Python
2*2
2 ** 3
20 / 4
20 // 4
20 % 4
## Learning data types 
## Integer data types are whole numbers 
## Numbers with decimal points are called floating-point numbers 
## Strings are text values, which are surrounded by single quotes ''
## Let's learn string concatenation
'Alice' + 'Bob' ## You can concatenate strings but you can't concatenate strings and integers
'Alice' * 5 ## This is string replication, repeating the original string by N times the integer value
## I am sure we know what is a variable in Python - it is basically storing information in the memory 
clippers = 93
mavericks = 96
total_score = clippers + mavericks
total_score
## A variable is created/initialised the first time you store a value into it. Thereafter, you can use it in subsequent exps
## When a variable is assigned a new value, the old value is overriden to the new value. 
## Variable names are important. A good name describes clearly the data it contains.
## There are 3 rules to naming variables. 
## a) It must be 1 word with no spaces, b) It can only use letters, numbers, and the underscore, c) It cannot start with number

## Let's create your 1st program 
## This program says hello and asks for my name 
print('Hello, world!')
print('What is your name?') ## Asks for name
my_name = input()
print('It is good to meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name))
print('What is your age?') ## Asks for age
my_age = input()
print('You will be ' + str(int(my_age) + 1) + ' in a year.')