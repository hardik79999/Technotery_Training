# Class Methods ---------------------------------

# Note: All methods must have self as the first parameter.

class Person:
    def __init__(self , name):
        self.name = name

    def display(self):
        print("Hello My Name Is "+ self.name)

p1 = Person("'HARDIK'")

p1.display() # Hello My Name Is 'HARDIK'


# Methods with Parameters --------------------------------------------


class Calculator:
    # Create a method with parameters:

    def add(self , a , b):
        return a + b

    def multi(self , a , b ):
        return a * b
    

obj = Calculator()

print(obj.add(5,5)) # 10
print(obj.multi(5,5)) # 25


# Methods Accessing Properties ----------------------------------------------------


class Student:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f"{self.name} is {self.age} Year Old")

s1 = Student("HARDIK",23)
print("-------------------------")
s1.get_info()


# Methods Modifying Properties -------------------------------------------------------


class My_info:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        self.age += 1
        print(f"Happy Brithday {self.name} ! You are now {self.age}")


my = My_info("HARDIK",22)
print("------------------------------------------")
my.display() # Happy Brithday HARDIK ! You are now 23



# The __str__() Method -----------------------------------------------------

# The __str__() method is a special method that controls what is returned when the object is printed:


# Without the __str__() method:
class Pepole:
    def __init__(self,name,age):
        self.name = name
        self.age = age

print("-----------------------------------")
p = Pepole("hardik",23)
print(p1) # <__main__.Person object at 0x00000221D99E6F90>

# With the __str__() method:

class xyz:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self): # return current object
        return f"{self.name} , {self.age}"
print("-----------------------------------")
x = xyz("hardik",23)

print(x) # hardik , 23


# Multiple Methods --------------------------------------------------

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self,song):
        self.songs.append(song) 
        print(f"Added : {song}")

    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed : {song}")

    def show(self):
        print(f"Playlist : {self.name}")
        for i in self.songs:
            print(f"- {i}")


my_playlist = Playlist("Favorites")
print("==================================================")
my_playlist.add_song("Dhurandhar - Title Track\n")
my_playlist.add_song("Dilbar Ki Aankhon Ka (From 'Thamma')\n")
my_playlist.remove_song("Dhurandhar - Title Track\n")
my_playlist.show()
print("==================================================")



class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil")

del Person.greet

p1.greet() # This will cause an error


