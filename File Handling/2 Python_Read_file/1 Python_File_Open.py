# Open a File on the Server --------------------------------------------------


f = open("demofile.txt")
print(f.read())

"""
To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:
"""


# If the file is located in a different location, you will have to specify the file path, like this:

# Example

# Open a file on a different location:

f = open(r"C:\Users\ASUS\OneDrive\Desktop\Write queries to create all the.txt")
print(f.read())



# Using the with statement ---------------------------------------------------


"""
You can also use the with statement when opening a file:

"""

print("---------------------------------------------------------------------------------------------------------------------------------")

with open("demofile.txt") as f:
    print(f.read())


# Close Files ----------------------------------------------------------

"""
It is a good practice to always close the file when you are done with it.

If you are not using the with statement, you must write a close statement in order to close the file:
"""

# Example
"""
Close the file when you are finished with it:
"""
print("---------------------------------------------------------------------------------------------------------------------------------\n")

f = open("demofile.txt") # read only frist line
print(f.readline()) # Fort Southerland is a redoubt built during the American Civil War to protect Camden,
f.close()
# After close the file
# print(f.read()) #ValueError: I/O operation on closed file.



# Read Only Parts of the File -----------------------------------------------

print("---------------------------------------------------------------------------------------------------------------------------------\n")

# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

with open("demofile.txt") as f:
    print(f.read(8)) # Fort Sou


# Read Lines ----------------------------------------------------------------

# You can return one line by using the readline() method:

with open("demofile.txt") as f:
    print(f.readline()) # Fort Southerland is a redoubt built during the American Civil War to protect Camden,


# By calling readline() two times, you can read the two first lines:

# Example

# Read two lines of the file:
print("---------------------------------------------------------------------------------------------------------------------------------\n")

with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())


# Loop through the file line by line:

with open("demofile.txt") as f:
    for i in f:
        print(i)