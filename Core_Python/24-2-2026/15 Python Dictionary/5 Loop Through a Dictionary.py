thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
    print(x) # get keys

# output :::
"""
brand
model
year
"""
print("---------------------------")

for x in thisdict:
    print(thisdict[x]) # get values

# output :::
"""
Ford
Mustang
1964
"""
print("------------------------------")

for x in thisdict.keys():
    print(x)


print("------------------------------")

for x, y in thisdict.items(): # gey key value pair
  print(x, y)

# output :::
"""
brand Ford
model Mustang
year 1964
"""