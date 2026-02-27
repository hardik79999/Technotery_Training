# Python range -----------------------------

# Creating ranges ---------------------------

# The range() function can be called with 1, 2, or 3 arguments, using this syntax:

# syntext :::
    # range(start, stop, step)



# Call range() With One Argument-----------------------------------------------

x = range(10)

# Call range() With Two Arguments ---------------------------------------------
x = range(3, 10)


# Call range() With Three Arguments --------------------------------------------
x = range(3, 10, 2)

# Using ranges----------------------------------------------

for i in range(10):
    print(i)


# Using List to Display Ranges -----------------------------------------

print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(range(1, 6))) # [1, 2, 3, 4, 5]
print(list(range(5, 20, 3))) # [5, 8, 11, 14, 17]



# Slicing Ranges-------------------------------------------------
r = range(10)
print(r[2])
print(r[:3])

# Membership Testing -------------------------------------------

r = range(0, 10, 2)
print(6 in r)
print(7 in r)

# Length ---------------------------------------

x = range(0,100,3)
print(len(x))