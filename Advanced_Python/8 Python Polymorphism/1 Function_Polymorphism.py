# # Function Polymorphism 

# # String -------------------------------------------------------------

# """
# For strings len() returns the number of characters:
# """
# # Example

# x = "Hello World!"

# print(len(x))

# # Tuple -----------------------------------------------------------------
# """
# For tuples len() returns the number of items in the tuple:
# """

# mytuple = ("apple", "banana", "cherry")

# print(len(mytuple))


# # Dictionary -----------------------------------------------------------

# """
# For dictionaries len() returns the number of key/value pairs in the dictionary:

# """

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(len(thisdict))


# # Class Polymorphism ------------------------------------------------------------------------


# """
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():
# """

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def Move(self):
#         print("Drive...!")
# class Boat:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def Move(self):
#         print("Saill...!")
# class Plane:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def Move(self):
#         print("Fly...!")


# Car1 = Car("Ford","mustang")
# Boat1 = Boat("Titanic","RMS")
# Plane1 = Plane("Boeing", "747")

# for i in (Car1,Boat1,Plane1):
#     i.Move()




# Inheritance Class Polymorphism -------------------------------------------------------------


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

print("---------------------------------------------")
for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
  print("------------")
