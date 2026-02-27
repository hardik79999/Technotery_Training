# Protected Properties ------------------------------------------------------
"""
Python also has a convention for protected properties using a single underscore _ prefix:
"""
# Example
"""
Create a protected property:
"""

class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) # Can access, but shouldn't

"""
Note: A single underscore _ is just a convention. It tells other programmers that the property is intended for internal use, 
but Python doesn't enforce this restriction.
"""

