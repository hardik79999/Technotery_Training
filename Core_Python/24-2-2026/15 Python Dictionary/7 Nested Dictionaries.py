myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily) # {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

print('---------------------------')


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


# Access Items in Nested Dictionaries ----------------------------------------------------------

print(myfamily["child2"]["name"]) # Tobias



# Loop Through Nested Dictionaries ------------------------------------------------
print("-----------------------------")
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

# output :::
"""
name: Emil
year: 2004
child2
name: Tobias
year: 2007
child3
name: Linus
year: 2011
"""