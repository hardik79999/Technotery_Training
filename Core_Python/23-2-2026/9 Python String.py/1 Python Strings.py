# Strings
print("hello")
print('hello')

#-------------------------------------------------------------------------
# Quotes Inside Quotes

print("hello ' broo")
print('hello " broo')
print("hello 'broo' ")


#-------------------------------------------------------------------------
# Assign String to a Variable

a = "hello"
print(a)
#-------------------------------------------------------------------------
# Multiline Strings

a = """
        MENU :::
    press (1) for pizza
    press (2) for burger

"""
print(a)
#-------------------------------------------------------------------------
# Strings are Arrays

a = "hardik bandhiya"
print(a[9])
print("------------------")

#-------------------------------------------------------------------------
# Looping Through a String

for i in "banana":
    print(i)

print("------------------")

#-------------------------------------------------------------------------
# String Length

a = "hardik bandhiya"
print(len(a))
#-------------------------------------------------------------------------

# check String

x = "hello world"
print("hello" in x)  # output : True

a = "hardik bandhiya"
if "hardik" in a:
    print("hardik present in sting")
else:
    print("Not present")

#-------------------------------------------------------------------------
# Check if NOT

a = "hello broo"
print("hardik" not in a)

a = "i am the best"
if "cool" not in a:
    print("'cool' is not present in string")

    