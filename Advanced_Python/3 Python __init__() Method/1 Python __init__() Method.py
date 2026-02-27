# The __init__() Method ----------------------------------------------------

class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age


obj = Person("hardik",23)

print(obj.name) # hardik
print(obj.age) # 23


# Why Use __init__()? --------------------------------------

"""
Without the __init__() method, you would need to set properties manually for each object:
"""

class Person2:
    pass


obj2 = Person2()

obj2.name = "hardik"
obj2.age = 23

print(obj2.name) # hardik
print(obj2.age)# 23


# With __init__(), you can set initial values when creating the object:

class data:
    def __init__(self , name , subject):
        self.name = name
        self.subject = subject

d1 = data("hardik","python")

print(d1.name) # hardik
print(d1.subject) # python


# Default Values in __init__() -------------------------------------------------------------

# You can also set default values for parameters in the __init__() method:

class person:
    def __init__(self , name , age , address = "junagadh"):
        self.name = name
        self.age = age
        self.address = address
        

p1 = person("hardik",23) # address is difault values
p2 = person("ravi",20) # address is difault values

print("--------------------------------")

print(p1.name,p1.age , p1.address) # hardik 23 junagadh
print(p2.name , p2.age , p2.address) # ravi 20 junagadh



# Multiple Parameters ---------------------------------------------------------

# The __init__() method can have as many parameters as you need:
print("----------------------------------------------------")

class info:
    def __init__(self , name , age , city , country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country


i = info("Hardik" , 23 , "Junagadh" , "India")

print(i.name) # hardik 
print(i.age)# 23
print(i.city) # junagadh
print(i.country) # India


