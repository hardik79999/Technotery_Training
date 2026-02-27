# Python has a built-in package called re, which can be used to work with Regular Expressions.


# Import the re module:
import re

# RegEx in Python  ---------------------------------------------

# When you have imported the re module, you can start using regular expressions:

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)


"""
RegEx Functions:

The re module offers a set of functions that allows us to search a string for a match:


Function	        Description

findall	            Returns a list containing all matches
search	            Returns a Match object if there is a match anywhere in the string
split	            Returns a list where the string has been split at each match
sub	                Replaces one or many matches with a string


"""

# The findall() Function ------------------------------------------

"""
The findall() function returns a list containing all matches.
"""

txt = "The rain in Spain"
x = re.findall("ai",txt)
print(x) # ['ai', 'ai']


txt = "The rain in india"
print(re.findall("spain",txt)) # Return an empty list if no match was found: []


# The search() Function ------------------------------------------------------------------

txt = "The Rain in spain"
x = re.search("\s",txt) # Search for the first white-space character in the string:

print("The first white-space character is located in position:", x.start())


# If no matches are found, the value None is returned:

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x) # none



# The split() Function ----------------------------------------------------------------

# The split() function returns a list where the string has been split at each match:


txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) # ['The', 'rain', 'in', 'Spain']


# Split the string only at the first occurrence:


txt = "The rain in Spain"
x = re.split("\s", txt, 1) 
print(x) # ['The', 'rain in Spain'] :: length : 2



# The sub() Function ----------------------------------------------------------------

# The sub() function replaces the matches with the text of your choice:

txt = "The rain in Spain"
x = re.sub("\s", "_", txt)
print(x) # The_rain_in_Spain


# Replace the first 2 occurrences:


txt = "The rain in Spain"
x = re.sub("\s", "_", txt, 2)
print(x) # The_rain_in Spain


# Match Object ------------------------------------------------------------------

# Do a search that will return a Match Object:
print("----------------------------------------------------")

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object





# Print the position (start- and end-position) of the first match occurrence.

# The regular expression looks for any words that starts with an upper case "S":


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())





# Print the string passed into the function:


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)



txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) # Spain

