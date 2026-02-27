# remove items --------------------------------------------------

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana") # If the item to remove does not exist, remove() will raise an error.

print(thisset) # {'apple', 'cherry'}




thisset = {"apple", "banana", "cherry"}

thisset.discard("banana") # If the item to remove does not exist, discard() will NOT raise an error.

print(thisset) # {'apple', 'cherry'}



# using POP ------------------------------------------------------

thisset = {"apple", "banana", "cherry"}

x = thisset.pop() # Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

print(x) # pop return remove items (element)

print(thisset) # {'banana', 'apple'}


# clear()

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset) # set()


thisset = {"apple", "banana", "cherry"}

del thisset # delete variable

print(thisset) # NameError: name 'thisset' is not defined