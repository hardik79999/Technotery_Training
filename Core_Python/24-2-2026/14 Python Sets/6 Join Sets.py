# Union

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) # {'a', 1, 'c', 2, 3, 'b'}


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2 # You can use the | operator instead of the union() method, and you will get the same result.
print(set3)



# Join Multiple Sets -------------------------------------------------

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4) # {'apple', 'a', 1, 2, 3, 'John', 'cherry', 'bananas', 'c', 'b', 'Elena'}
print(myset)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)