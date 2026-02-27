def my_function():
    print("Hello from a function")


def my_function():
    print("Hello from a function")

my_function()



def my_function():
    print("Hello from a function")

my_function() # output : Hello from a function
my_function() # output : Hello from a function
my_function() # output : Hello from a function



# Function Names ------------------------------

"""
calculate_sum()
_private_function()
myFunction2(
"""

# Without Functions

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)


# With Functions

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# Output :::
"""
25.0
35.0
10.0
"""

# Return Values ------------------------------

def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)


# Parameters vs Arguments -----------------------------

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument


# Default Parameter Values -----------------------------

def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function() # friend
my_function("Linus")