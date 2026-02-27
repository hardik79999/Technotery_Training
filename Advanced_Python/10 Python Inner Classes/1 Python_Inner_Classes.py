class Outer:
    def __init__(self):
        self.name = "Outer class"

    class Inner:
        def __init__(self):
            self.name = "Inner class"

        def display(self):
            print("Ths is Inner class")

obj = Outer()
print(obj.name)

print("--------------------------------------")


class Outer:
    def __init__(self):
        self.name = "Outer class"

    class Inner:
        def __init__(self):
            self.name = "Inner class"

        def display(self):
            print("Ths is Inner class")

obj = Outer()
print(obj.name)
obj.Inner().display()




print("--------------------------------------")

class Outer:
    def __init__(self):
        self.name = "Outer class"

    class Inner:
        def __init__(self):
            self.name = "Inner class"

obj = Outer()
print(obj.name)

print(obj.Inner().name)


print("--------------------------------------")


# Accessing Inner Class from the Outside -----------------------------------------------

class Outer:
  def __init__(self):
    self.name = "Outer"

  class Inner:
    def __init__(self):
      self.name = "Inner"

    def display(self):
      print("Hello from inner class")

outer = Outer()
inner = outer.Inner()
inner.display()


print("--------------------------------------")

# Accessing Outer Class from Inner Class --------------------------------------------------


class Outer:
  def __init__(self):
    self.name = "Emil"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()


# Practical Example ---------------------------------------------------

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
            self.status = "off"
            print("Engine Start...")
        
        def start(self):
           self.status = "Running".lower()
           print("Engine running...")
        def stop(self):
           self.status = "off"
           print("Engine Stoped...")
    def drive(self):
        if self.engine.status == "running": # self.Engine()
            print(f"Driving the {self.brand} {self.model}")

        else:
           print("Start the engine first!")

car = Car("Mahindra","Thar")
print("-----------------------------------------------")
car.drive()
car.engine.start()
car.drive()


# Multiple Inner Classes -----------------------------------------------------


class Computer:
  def __init__(self):
    self.cpu = self.CPU()
    self.ram = self.RAM()

  class CPU:
    def process(self):
      print("Processing data...")

  class RAM:
    def store(self):
      print("Storing data...")

computer = Computer()
computer.cpu.process()
computer.ram.store()
