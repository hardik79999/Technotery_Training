"""
None is a special constant in Python that represents the absence of a value.

Its data type is NoneType, and None is the only instance of a NoneType object.
"""

# NoneType ----------------------------------------------------

# Assign and display a None value:

x = None
print(x)
print(type(x)) # <class 'NoneType'>

result = None
if result is None:
    print("No result yet") # No result yet
else:
    print("Result is ready")


result = None
if result is not None:
  print("Result is ready")
else:
  print("No result yet") # No result yet



print(bool(None)) # False


# Functions returning None ------------------------------------------

def myfunc():
    x = 5

x = myfunc()
print(x) # none

