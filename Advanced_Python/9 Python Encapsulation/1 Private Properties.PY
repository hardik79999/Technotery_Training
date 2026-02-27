# Private Properties -------------------------------------------------------
"""
In Python, you can make properties private by using a double underscore __ prefix:
"""
# Example
"""
Create a private class property named __age:
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # Private property

p1 = Person("Hardik", 23)
print(p1.name)
# print(p1.__age) # This will cause an error   # Note: Private properties cannot be accessed directly from outside the class.



# Get Private Property Value -------------------------------------------------------

class Person:
    def __init__(self, name , age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age 

p1 =  Person("Hardik", 23)
print("------------------------------------------")
print(p1.get_age()) # 23



# Set Private Property Value -----------------------------------------


class data:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age
    

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age is Nagative")

p1 = data(23)
print("-------------------------------------")
print(p1.get_age())


p1.set_age(77)
print(p1.get_age())


# Why Use Encapsulation? -------------------------------------------------------------
"""
Encapsulation provides several benefits:

"""
"""
Data Protection: Prevents accidental modification of data
Validation: You can validate data before setting it
Flexibility: Internal implementation can change without affecting external code
Control: You have full control over how data is accessed and modified
"""

class Student:

    def __init__(self,name):
        self.name = name
        self.__grade = 0

    def set_grade(self,grade):
        if grade > 0  and grade <= 100:
            self.__grade = grade
        else:
            print("Invalid Grade")
    
    def get_grade(self):
        return self.__grade
    
    def get_status(self):
        if self.__grade >= 60:
            return "Passed"
        else:
            return "Fail"
        
s1 = Student("name")
print("---------------------------------------")
print(s1.name)
s1.set_grade(88)
print(s1.get_grade())
print(s1.get_status())
print("---------------------------------------")

# Output :::
"""
name
88
Passed
"""