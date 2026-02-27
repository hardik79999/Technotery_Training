# Create a Class ---------------------------------------------

class MyClass:
    x = 5

# Create Object

p1 = MyClass()
print(p1.x)


# Delete Objects ------------------------------------------------------------------

# del p1
print(p1) # NameError: name 'p1' is not defined


# Multiple Objects -----------------------------------------------


p4 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)


# The pass Statement --------------------------------------

class Person:
    pass


