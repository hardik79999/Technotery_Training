# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.


# Create a Parent Class --------------------------------------

# Create a class named Person, with firstname and lastname properties, and a printname method:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Hardik", "Bandhiya")
x.printname()


# Create a Child Class ------------------------------------------------------------------

# Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
    pass

# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.


# Use the Student class to create an object, and then execute the printname method:

class Person:
    def __init__(self,name , age ):
       self.name = name
       self.age = age

class Student(Person):
   def display(self):
      print(f"Name {self.name}\nAge : {self.age}")

obj = Student("hardik",23)

print("---------------------------------------")

obj.display()


# Add the __init__() Function -----------------------------------------------
"""
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

Note: The __init__() function is called automatically every time the class is being used to create a new object.
"""
# Example

# Add the __init__() function to the Student class:
"""
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc."""


# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

# Example

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)


# Use the super() Function ---------------------------------------------------------------

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(self , fname, lname)

"""By using the super() function, you do not have to use the name of the parent element, 
it will automatically inherit the methods and properties from its parent."""


# Add Properties -----------------------------------------------------

# Example

# Add a property called graduationyear to the Student class:
"""
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019"""


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

print("----------------------------------------")

print(x.graduationyear)


# Add Methods -----------------------------------------------------

# Add a method called welcome to the Student class:

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Hardik", "Bandhiya", 2024)
x.welcome()