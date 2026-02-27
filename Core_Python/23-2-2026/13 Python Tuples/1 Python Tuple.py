thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Allow Duplicates-----------------------------------
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) # output : ('apple', 'banana', 'cherry', 'apple', 'cherry')

# Tuple Length---------------------------------------
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) # output 3



# Create Tuple With One Item------------------------------------------
thistuple = ("apple",)
print(type(thistuple)) # output : <class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) # output : <class 'str'>


# Tuple Items - Data Types----------------------------------------
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)