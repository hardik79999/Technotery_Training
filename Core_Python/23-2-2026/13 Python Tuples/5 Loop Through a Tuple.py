thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)


"""
output :
apple
banana
cherry
"""

# Loop Through the Index Numbers ---------------------------------
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])


"""
output :
apple
banana
cherry
"""
    
# Using a While Loop----------------------
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1


"""
output :
apple
banana
cherry
"""