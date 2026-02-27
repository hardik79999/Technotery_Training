# Set

thisset = {"apple","banana","cherry"} # unordered

print(thisset) #output : {'banana', 'apple', 'cherry'}


# Duplicates Not Allowed ---------------------------------

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) # output : {'cherry', 'apple', 'banana'}


thisset = {"apple", "banana", "cherry", True, 1, 2} # True and 1 is considered the same value:

print(thisset) # output : {True, 2, 'banana', 'cherry', 'apple'}



thisset = {"apple", "banana", "cherry", False, True, 0} # False and 0 is considered the same value:

print(thisset)



myset = {"apple", "banana", "cherry"}
print(type(myset)) # output : <class 'set'>