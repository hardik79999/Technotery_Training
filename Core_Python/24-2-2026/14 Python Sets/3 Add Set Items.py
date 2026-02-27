# using (.add)

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) # output : {'apple', 'orange', 'banana', 'cherry'}


# Add Sets ------------------------------------

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset) # output : {'papaya', 'apple', 'pineapple', 'cherry', 'mango', 'banana'}



# Add Any Iterable-------------------------------------------------

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset) # {'banana', 'orange', 'kiwi', 'apple', 'cherry'}