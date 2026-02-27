# Remove Specified Item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # output : ['apple', 'cherry']


# Remove Specified Index---------------------------------------------------------

thislist = ["apple", "banana", "cherry"]
thislist.pop() # by default remove last index value
print(thislist) # output L ['apple', 'banana']


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # output : ['apple', 'cherry']


# using (del) keyword delete items in list---------------------------------------------------------

thislist = ["apple", "banana", "cherry"]
del thislist[2]
print(thislist) # output : ['apple', 'banana']

thislist = ["apple", "banana", "cherry"]
del thislist # delete all items in list
# print(thislist) # NameError: name 'thislist' is not defined


# Clear the List---------------------------------------------------------

thislist = ["apple", "banana", "cherry"]
thislist.clear() # remove all items in list and return empy list
print(thislist) # output : []