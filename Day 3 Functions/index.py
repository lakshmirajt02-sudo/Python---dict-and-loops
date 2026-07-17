# FUNCTION 
# --------
def func_name(parameters):
   pass

# greet() no hoisting in python
# def greet():
#    print('Hello Python')
# greet()     

# def add(a, b):
#    print("sum: ", a + b)      
# add(10, 5)

# function scope 
# --------------
# 1. local scope 
# 2. global scope 

# def sum():
#    # local scope
#    count = 0
#    print(count)

# global scope 
# count = 0
# def sum():
#    print(count)

# FUNCTION ARGUMENTS 
# ------------------
# 1. Required / Positional arguments 
# 2. Default arguments 
# 3. Keyword arguments 
# 4. Arbitary arguments 
# 5. Arbitary keyword arguments 

# required argument 
# def add(a, b):
#    print("sum: ", a + b)      
# add(10, 5)

# Default arguments
# def greet(name, age=18):
#    print(f"my name is {name} and age is {age}")
# greet('John')

# def greet(name, age=18):
#    print(f"my name is {name} and age is {age}")
# greet('John', 50)

# Keyword arguments - there will be no problem if the position of argument has changed..shows same o/p
# def students(first_name, last_name):
#    print(first_name , last_name)
# students(first_name="john", last_name="doe")
# students( last_name="doe", first_name="john")

# Arbitary arguments  - return a tuple
# def my_fun(*args):
#    sum = 0
   # print(args) o/p (1, 2, 3, 4, 5)
#    for i in args:
#       sum += i 
#    print(sum)
# my_fun(1, 2, 3, 4, 5)

# def myFun(*args):
#    for i in args:
#       print(i)
# myFun('Hello', 'Welcome', 'To', 'GeeksForGeeks')

# Arbitary keyword arguments -> returns a dict also uses  ** in parameter
# def students(**kwargs):
#    print(kwargs)
#    print(kwargs['first_name'])
# students(first_name="Poopy", last_name="Panda", email="johndoe@gmail.com")

# return statement 
# def add(a , b):
#    return a + b
# print(add(20 , 10))




   