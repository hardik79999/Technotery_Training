# Python has a built-in package called json, which can be used to work with JSON data.  

import json


# Parse JSON - Convert from JSON to Python  --------------------------------------

"""
If you have a JSON string, you can parse it by using the json.loads() method.
"""

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])



# Convert from Python to JSON -------------------------------------------------------------------------


# a Python object (dict):
x = {
  "name": "hardik",
  "age": 23,
  "city": "Junagadh"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:

print(y) # {"name": "hardik", "age": 23, "city": "Junagadh"}
print(type(y)) # <class 'str'>

"""
You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None

"""
# Convert Python objects into JSON strings, and print the values:

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
print(type(x)) # <class 'dict'>



# Format the Result ----------------------------------------------------------

print(json.dumps(x, indent=4, separators=(". ", " = "))) # Use the separators parameter to change the default separator:

# Output :::

"""
{
    "name" = "John".
    "age" = 30.
    "married" = true.
    "divorced" = false.
    "children" = [
        "Ann".
        "Billy"
    ].
    "pets" = null.
    "cars" = [
        {
            "model" = "BMW 230".
            "mpg" = 27.5
        }.
        {
            "model" = "Ford Edge".
            "mpg" = 24.1
        }
    ]
}
"""

print(json.dumps(x, indent=4)) # Use the indent parameter to define the numbers of indents:

# Output :::

"""
{
    "name": "John",
    "age": 30,
    "married": true,
    "divorced": false,
    "children": [
        "Ann",
        "Billy"
    ],
    "pets": null,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
}
"""

print("----------------------------------------------------")

print(json.dumps(x, indent=4, sort_keys=True)) # Use the sort_keys parameter to specify if the result should be sorted or not:
# Output :::

"""
{
    "age": 30,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ],
    ],
    ],
    "children": [
        "Ann",
        "Billy"
    ],
    "divorced": false,
    "married": true,
    "name": "John",
    "pets": null
}   
"""