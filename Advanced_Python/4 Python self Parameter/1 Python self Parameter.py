# The self Parameter ----------------------------------------

# The self parameter is a reference to the current instance of the class.

class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def myfun(self):
        print("My Name is : " + self.name)


obj = Person("hardik",23)

obj.myfun()

"""
Note: The self parameter must be the first parameter of any method in the class.
"""


# Why Use self? ---------------------------------------------------

# Without self, Python would not know which object's properties you want to access:

# The self parameter links the method to the specific object:

class info:
    def __init__(self , name):
        self.name = name

    def printname(self):
        print("My Name is : ",self.name)

print("------------------------------------")

p1 = info("Hardik")
p2 = info("Ravi")

p1.printname() # My Name is :  Hardik
p2.printname() # My Name is :  Ravi



# Accessing Properties with self -------------------------------------------------------

class CAR:
    def __init__(self , brand , model , year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(f"Brand : {self.brand}\nModel : {self.model}\nYear : {self.year}")


c1 = CAR("Mahindra","Thar",2025)
print("------------------------")
c1.display()


# Calling Methods with self -----------------------------------

# Call one method from another method using self:

class data:
    def __init__(self , name):
        self.name = name

    def p1(self):
        return "Hello "+ self.name
    
    def welcome(self):
        p_nam = self.p1()
        print(p_nam + " Welcom to our Website ...")


data1 = data("HARDIK")
print("----------------------------------")
data1.welcome() # Hello HARDIK Welcom to our Website ...


class info:
    def __init__(self,name):
        self.name = name
    def dispaly(self):
        print("hello "+self.name)


# Create an object
obj = info("hardik")
# Call the show method
obj.dispaly()