
# without Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) # output : ['apple', 'banana', 'mango']



# using Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) # output : ['apple', 'banana', 'mango']



# The Syntax

# newlist = [expression for item in iterable if condition == True]

newlist = [x for x in range(10) if x < 5]
print(newlist) # output : [0, 1, 2, 3, 4]

newlist = ['hello' for x in fruits]
print(newlist) # output : ['hello', 'hello', 'hello', 'hello', 'hello']

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist) #output : ['apple', 'orange', 'cherry', 'kiwi', 'mango']


num = [1,2,3,4,5,6]
new = [x if x >3 else "lower"for x in num]
print(new) # output : ['lower', 'lower', 'lower', 4, 5, 6]