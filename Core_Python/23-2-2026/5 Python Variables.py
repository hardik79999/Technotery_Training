x = 5 # x type is int 
y = "Hardik" # y type is str 

print(x)
print(y)

#---------------------------------------------------------------------------------------
# Casting

x = int(5)
y = str(10)
z = float(3) # Output : 3.0

print(x)
print(y)
print(z)


#---------------------------------------------------------------------------------------
x = 90
y = "hello"
z = True
a = 3.14
print(type(x)) # output : <class 'int'>
print(type(y)) # output : <class 'str'>
print(type(z)) # output : <class 'bool'>
print(type(a)) # output : <class 'float'>

#---------------------------------------------------------------------------------------
# Case-Sensitive

a = 3
# A will Not Overwrite a
A = "hello"

#---------------------------------------------------------------------------------------
# Variable Names
 
# valid variable name
myvar = "hardik"
my_var = "hardik"
_my_var = "hardik"
myvar = "hardik"
Myvar = "hardik"
Myvar2 = "hardik"

# invalid variable name
# 2myvar = "hardik"
# my-var = "hardik"
# my var = "hardik"


#---------------------------------------------------------------------------------------
# Assign Multiple Values

# 1 multiple variable
x,y,z = "orange","banana","apple"
print(x) # Output : orange
print(y) # Output : banana
print(z) # Output : apple
print(x,y,z) # output : orange banana apple

# one value multiple variable

x = y = z = "apple"
print(x) #output : apple
print(y) #output : apple
print(z) #output : apple

#---------------------------------------------------------------------------------------
# Output Variables

x = "python is best"
print(x)

# multiple variable saprated comma
x = "python"
y = "is"
z = "best"

print(x,y,z) # output : python is best

# use the + operator to output multiple variables:

x = "python " # use end with space ' '
y = "is "
z = "best "

print(x + y + z) # output : python is best

# mathematical operator
x = 5
y = 10
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y) # remove . value

x = 5
y = "hardik "
# print(x+y) # output : TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(x,y) #otput : 5 hardik

print(x*y) # output : hardik hardik hardik hardik hardik


#---------------------------------------------------------------------------------------
# Global Variables

x = "hardik" # Create a variable outside of a function and use it inside the function

def myfun():
    print("my name is " + x)

myfun() # output : my name is hardik

print("----------------")

x = "hardik"

def myfun():
    x = "bandhiya"
    print("my surname is " + x)

myfun() # output : my surname is bandhiya
print("my name is " + x) # output : my name is hardik
#---------------------------------------------------------------------------------------
# Variable Exercises

#---------------------------------------------------------------------------------------