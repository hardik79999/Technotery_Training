thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # output: ['apple', 'banana', 'cherry', 'orange']


# Insert Items

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) # output : ['apple', 'orange', 'banana', 'cherry']


# Extend List


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # output : ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


# Add Any Iterable

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)