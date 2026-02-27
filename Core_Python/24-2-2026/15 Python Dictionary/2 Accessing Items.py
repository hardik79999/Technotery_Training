thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

print(x) # Mustang

x = thisdict.get("model") # here is also a method called get() that will give you the same result:
print(x) # Mustang


# Get Keys ---------------------------------

x = thisdict.keys() # get only  key
print(x) # dict_keys(['brand', 'model', 'year'])

x = thisdict.values() # ger only value
print(x) # dict_values(['Ford', 'Mustang', 1964]) 

x = thisdict.items() # get key value pair
print(x) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
y = car.values()

print(x) # dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x) # dict_keys(['brand', 'model', 'year', 'color'])
print(y) # dict_values(['Ford', 'Mustang', 1964, 'white'])