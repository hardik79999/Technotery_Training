
# Dictionaries

thisdict = {
  "brand": "Ford",    # Dictionaries are used to store data values in key:value pairs.
  "model": "Mustang",
  "year": 1964
}
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}



# Dictionary Items ---------------------------------------------

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"]) # Ford


# Duplicates Not Allowed -----------------------------------------------

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Dictionary Length

print(len(thisdict)) # 3



# Dictionary Items - Data Types --------------------------------------------

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict) # {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

# The dict() Constructor ---------------------------------------------------------

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) # {'name': 'John', 'age': 36, 'country': 'Norway'}