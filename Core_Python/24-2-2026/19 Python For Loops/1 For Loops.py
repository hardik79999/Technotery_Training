fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

"""
apple
banana
cherry
"""


# Looping Through a String ----------------------

for x in "banana":
    print(x)
"""

b
a
n
a
n
a
"""

# The break Statement ---------------------------------

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

print("-----------------------------")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


# The range() Function ---------------------------------

for x in range(6):
    print(x) 

"""
0
1
2
3
4
5
"""
print("----------------------------------")
for x in range(2, 30, 3):
    print(x)


# Else in For Loop --------------------------------------------
print("----------------------------------")

for x in range(6):
    print(x)
else:
    print("Finally finished!")

print("----------------------------------")

for x in range(6):
    if x == 3: 
        break
    print(x)
else:
    print("Finally finished!")


# Nested Loops -------------------------------------

print("----------------------------------")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


# The pass Statement --------------------------------------

for x in [0, 1, 2]:
    pass # for loops cannot be empty, but if you for some reason have a 
         # for loop with no content, put in the pass statement to avoid getting an error.