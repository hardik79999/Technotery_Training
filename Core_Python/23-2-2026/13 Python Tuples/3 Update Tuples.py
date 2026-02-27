# Change Tuple Values
"""
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

"""

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) # output : ('apple', 'kiwi', 'cherry')


# Add Items---------------------------------------------------

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)  # output : ('apple', 'kiwi', 'cherry')


# Add tuple to a tuple.

"""
You are allowed to add tuples to tuples, so if you want to add one item, (or many),
create a new tuple with the item(s), and add it to the existing tuple:

"""

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple) # output : ('apple', 'banana', 'cherry', 'orange')

# Remove Items------------------------------------------
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple) # output : ('banana', 'cherry')

# use delete--------------------------------------------

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
