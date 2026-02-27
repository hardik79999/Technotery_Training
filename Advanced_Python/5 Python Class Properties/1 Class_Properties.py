# Class Properties--------------------------------------------

# Properties are variables that belong to a class. They store data for each object created from the class.

class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

obj = Person("HARDIk",23)

print(obj.name)
print(obj.age)


# Access Properties -----------------------------------


class CAR:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    
car1 = CAR("Toyota","Fortuner")
print("--------------------------")
print(car1.brand) # Toyota
print(car1.model) # Fortuner


# Modify Properties  ----------------------------------------------

# You can modify the value of properties on objects:

# Change the age property:

class data:
    def __init__(self , name , age):
        self.name = name
        self.age = age


p1 = data("HARDIK",20)
print("'''''''''''''''''''''''''''''''''''''''")
print(p1.name)
# Before
print(p1.age) # 20
# After
p1.age = 23
print(p1.age) # 23


# Delete Properties ----------------------------------------------------


p2 = data("HARDIK",23)


del p2.age
print("------------------------------------------")
print(p2.name)
# print(p2.age) # AttributeError: 'data' object has no attribute 'age'



# Class Properties vs Object Properties  -------------------------------------------

class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("HARDIK")
p2 = Person("RAVI")
p3 = p2 # Shere thr object for class
print("----------------------------------------------")
print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)
print(p3.species) # use


# Modifying Class Properties ---------------------------------------

class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"
print("----------------------------------------------")
print(p1.lastname)
print(p2.lastname)


# Add New Properties ----------------------------------------------

class ABC:
   def __init__(self , name):
      self.name = name

    
k = ABC("HARDIK")
print("---------------------------------")
k.age = 23 # add new property at the object
k.city = "junagadh" # add new property at the object

print(k.name) # hardik
print(k.age) # 23
print(k.city) # junagadh


